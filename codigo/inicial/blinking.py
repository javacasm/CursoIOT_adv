import machine
import time

v = 0.4 # Gracias Kiko

PIN_LED_PLACA = 2 # en otras placas puede ser el 4

# setup en arduino
led = machine.Pin(PIN_LED_PLACA, machine.Pin.OUT)


def parpadeo(tiempo_encendido = 250,tiempo_apagado = 250):
    # tiempos en milisegundos
    led.on()
    time.sleep_ms(tiempo_encendido)  # en milisegunos
    led.off()
    time.sleep_ms(tiempo_apagado)   # en milisegunos
# se acaba la función

def blinking_forever():
    while True :  # bucle loop en arduino
        parpadeo()
        
        # esta en el bucle
#fuera de la función
