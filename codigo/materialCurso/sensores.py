import dht
import machine
import time

DHT_pin=14
v=0.3

sensor =dht.DHT22(machine.Pin(DHT_pin))

def showSensorData():
    sensor.measure()
    print('Temp=',sensor.temperature(),'Hum=',sensor.humidity())
    
    
def showSensorData_forever():
    while True:
        showSensorData()
        time.sleep(1)