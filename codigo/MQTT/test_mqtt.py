import umqttsimple
import ubinascii
import machine
import time
import dht

v = 0.5

client_id = ubinascii.hexlify(machine.unique_id())

topic_Temp = b'/salon/DHT22_TEMP'
topic_Hum = b'/salon/DHT22_HUM'
topic_LED = b'/salon/LED'
topic_errors = b'/errors'

PIN_DHT = 15
BUILTIN_LED = 2

dht22 = dht.DHT22(machine.Pin(PIN_DHT))

led = machine.Pin(BUILTIN_LED, machine.Pin.OUT)

def sub_CheckTopics(topic, msg):
    print(f'Topic:{topic} msg:{msg}')
    if topic == topic_LED:     # Check for Led Topic
        if msg == b'On':
            led.on()
            print('Led:On')
        elif msg == b'Off':
            led.off()
            print('Led:Off')
        else:
            print('Led unkown message: {msg}')
            
def getLocalTimeHumanFormat():
    strLocalTime = "{0}/{1:02}/{2:02} {3:02}:{4:02}:{5:02}".format(*time.localtime(time.time())[0:6])
    return strLocalTime

def publish_forever(tiempo = 10):
    client = umqttsimple.MQTTClient(client_id, '192.168.1.65', port = 1883)
    client.set_callback(sub_CheckTopics)
    try:
        client.connect()
        client.subscribe(topic_errors)
        print(f'Suscrito a {topic_errors}')
        client.subscribe(topic_LED)
        print(f'Suscrito a {topic_LED}')
    except umqttsimple.MQTTException as me: # https://www.vtscada.com/help/Content/D_Tags/D_MQTT_ErrMsg.htm
        value = f'{me}'
        if value == '5':
            print('Error de autorizacion')
        elif value == '4':
            print('Login error')
        else:
            print(f'Error conectando: {me}')
        time.sleep(10)
        machine.reset()
    except Exception as e:
        print(f'Error conectando (ex): {e}')
        time.sleep(10)
        machine.reset()

    last_Temp = 0 # utime.ticks_ms()
    while True :

        now = time.ticks_ms()
        elapsedTime = time.ticks_diff(now, last_Temp)
        client.check_msg() # comprobamos si hay mensajes para nosotros
        
        if elapsedTime > (tiempo * 1000):
            last_Temp = now
            msgTime = getLocalTimeHumanFormat()
            try:
                dht22.measure()
                # Con más formato ...
                temp = dht22.temperature()
                hum = dht22.humidity()
                client.publish(topic_Temp, f'{temp}')
                client.publish(topic_Hum, f'{hum}')
                print( f'{msgTime} publicado {topic_Temp} - {temp} - {topic_Hum} - {hum}')
            
            except Exception as e:
                print(f'Error publicando: {e}')
        time.sleep_ms(10)
