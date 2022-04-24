import machine
import time
v=0.2
led= machine.Pin(2, machine.Pin.OUT)
def parpadeo(tiempo_encendido = 250,tiempo_apagado =250):
    led.on()
    time.sleep_ms(tiempo_encendido)#milisegundos
    led.off()
    time.sleep_ms(tiempo_apagado) #milisegundos
    
def blinking_forever():
    while True :
        parpadeo()