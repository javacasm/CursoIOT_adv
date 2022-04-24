import machine
import dht
import time

PIN_RELE = 4
PIN_DHT = 12

rele = machine.Pin(PIN_RELE, machine.Pin.OUT)

sensor = dht.DHT22(machine.Pin(PIN_DHT))

def ventilador():
    
    sensor.measure()
    print('Temp:',sensor.temperature(),'Hum: ',sensor.humidity())
    if sensor.temperature() > 24 :
        rele.on()  # encendemos el ventilador
        print('Encedemos el rele')
    else :
        rele.off()  # apagamos el ventilador
        print('Apagamos el rele')
#    time.sleep(1)
    
