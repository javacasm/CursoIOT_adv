import test_dht
import blinking
import time
import ventiladorDomotico

v=0.1

print('Medimos la temperatura y la humedad y parpadeamos')

while True:
    #test_dht.showSensorData()
    blinking.parpadeo()
    ventiladorDomotico.ventilador()
    time.sleep(1)