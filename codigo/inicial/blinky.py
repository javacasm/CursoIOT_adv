# Blinky
import machine
import time

v = 0.1

led = machine.Pin(2,machine.Pin.OUT)
while True:
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.1)
