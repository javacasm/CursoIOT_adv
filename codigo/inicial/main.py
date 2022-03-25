import test_dht
import blinking
import time

v = 0.2

print('Medimos la temperatura y la humedad y parpadeamos')

while True:
    test_dht.showSensorData()
    blinking.parpadeo()
    time.sleep(0.5)