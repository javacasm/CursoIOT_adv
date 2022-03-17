## Medida de temperatura, humedad y presion ocn sensor BME280 ma
import machine # Usaremos los pines y el I2C
import BME280  # Importamos la clase BME280


def testBME280():
    i2c = machine.SoftI2C(sda = machine.Pin(22),scl = machine.Pin(21)) # configuramos el acceso al bus i2c 
    devs = i2c.scan() # Comprobamos que se detecta el dispositivo en la direccion 0x76 (118) 
    if len(devs)>0:
        for dev in devs:
            print(hex(dev))
    else:
        print('No se ha encontrado ningún dispositivo')
    bme = BME280.BME280(i2c = i2c, address=0x77) 
    print('Temp: '+str(bme.temperature) + ' Pres: '+ str(bme.pressure) + ' Hum: '+str(bme.humidity))



