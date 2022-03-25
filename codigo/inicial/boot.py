# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import network
import time
import machine
import blinking 


SSID = 'OpenWrt'
WIFI_PASSWD = 'qazxcvbgtrewsdf'

w = network.WLAN(network.STA_IF)
if not w.active(): # evita el error OSError de intentar activar si ya activa
    w.active(True)  
    
if not w.isconnected():
    print('Conectando a ',SSID)
    w.connect(SSID, WIFI_PASSWD)
    while not w.isconnected():
        print('.', end='')
        blinking.parpadeo(tiempo_encendido=100,tiempo_apagado=100)
        time.sleep(0.1)
        
print('Conectado con IP:',w.ifconfig()[0]) # imprimimos sólo el primer elemento que es la ip

#import webrepl
#webrepl.start()

