# Fichero de configuracion

v = '0.5'

SSID = 'OpenWrt'
PASSWD_WIFI = 'qazxcvbgtrewsdf'

DEEP_SLEEP = True

mqtt_server = 'io.adafruit.com'
mqtt_port =  1883
mqtt_user = 'javacasm'
mqtt_password = 'aio_ukEn96IjNxu7bOlFaQiTmkELJp2E'

BOARD = 'Wemos Battery'

LED_INVERTED = True
pin_led_builtIn = 16
'''
16 para wemos battery
2 para wemos R32 D1
22 para Lolin32 Lite
'''

print(f'Using config for board: {BOARD}')

