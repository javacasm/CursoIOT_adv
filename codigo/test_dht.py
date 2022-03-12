# Test dht
import dht
import machine
import time

v = 0.3

PIN_DHT = 15

dht22 = dht.DHT22(machine.Pin(PIN_DHT))

while True:
    try:
        dht22.measure()
        # Con más formato ...
        print(f'Temp: {dht22.temperature():2.1f} C ')
        print(f'Hum: {dht22.humidity():2.2f} % ')
    except Exception as e:
        print(f'Error: {e}')
    time.sleep(1)

