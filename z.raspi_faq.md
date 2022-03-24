
## ¿raspberrypi.org o raspberrypi.com?


## Versión instalada ¿32 o 64?

```sh
$  uname -a
Linux rasp40064 5.10.103-v8+ #1530 SMP PREEMPT Tue Mar 8 13:06:35 GMT 2022 aarch64 GNU/Linux

```
La parte relevante es aarch64 que define la arquitectura: arm 64 bits (que podemos obtener con "uname -m")

## Instalación de Arduino



## Instalación de snap



## Instalación de Telegram-desktop

## Instalación Visual Studio Code

[Descargamos el fichero deb de la versión de ARM o ARM64](https://code.visualstudio.com/#alt-downloads)

y lo instalamos

```sh
sudo dpkg -i Downloads/code_1.65.2-1646927742_amd64.deb
```

o desde [snap-store](https://snapcraft.io/code)

```sh
sudo snap install code --classic
```

## Conectar con github


## Instalación de Prusa Slicer

A día de hoy (marzo 2022) no hay una versión oficial de PrusaSlicer para Raspberry, pero podemos instalar una versión no-oficial pero que funciona bien


Instalamos FUSE (necesario para ejecutar appimage) y algunas librerías necesarias para que fncione:

```sh
sudo apt-get install libfuse2  imagemagick fuse
```
Descargamos el ejecutable en formato [appimage](https://github.com/davidk/PrusaSlicer-ARM.AppImage/releases) (en mi caso la versión de 64 bits)

Le damos permisos de ejecución:

```sh
mv ~/Downloadas/PrusaSlicer-version_2.4.1-aarch64.AppImage ~/
chmod u+x ~/PrusaSlicer-version_2.4.1-aarch64.AppImage

~/PrusaSlicer-version_2.4.1-aarch64.AppImage
```

## Configuración de MQTT 

Configuración para acceso desde fuera

## Fritzing

sudo apt install fritzing


## Configuración pantalla

[configuración](https://pimylifeup.com/raspberry-pi-screen-resolution/#:~:text=With%20the%20tool%20loaded%20on,set%20for%20this%20current%20display.)

## Memoria libre

```sh
free -h
```

[documentación](https://forums.raspberrypi.com/viewtopic.php?t=269405)

### DDNS

https://www.noip.com/es-MX/remote-access

## ssh

[Activación de ssh desde la tarjeta](https://howchoo.com/g/ote0ywmzywj/how-to-enable-ssh-on-raspbian-without-a-screen)

## wifi

[configuración de wifi desde tarjeta](https://howchoo.com/g/ndy1zte2yjn/how-to-set-up-wifi-on-your-raspberry-pi-without-ethernet)
