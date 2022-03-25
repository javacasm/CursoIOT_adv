# Test dht
import dht
import machine
import time

v = 0.3

PIN_DHT = 15

dht22 = dht.DHT22(machine.Pin(PIN_DHT))

def showSensorData():
    dht22.measure() # hace la medida
    print('Temp:',dht22.temperature(),'Hum: ',dht22.humidity())


def showSensorDataForever(tiempo = 1):
    while True:
        showSensorData()
        time.sleep(tiempo)

