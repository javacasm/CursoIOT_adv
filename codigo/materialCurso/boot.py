import network
import time
wifi=network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect('SALON-ACTOS','CEPMONTILLA')
while not wifi.isconnected():
    print('.')
    time.sleep(1)

print(wifi.ifconfig())