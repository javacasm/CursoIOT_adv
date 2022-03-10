# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import network
import time
import machine

led = machine.Pin(2,machine.Pin.OUT)
w = network.WLAN(network.STA_IF)
if not w.active():
    w.active(True)
    
if not w.isconnected():
    w.connect('OpenWrt','qazxcvbgtrewsdf')
    while not w.isconnected():
        print('.')
        led.value(not led.value())
        time.sleep(0.5)
print('IP:',w.ifconfig()[0])

#import webrepl
#webrepl.start()
