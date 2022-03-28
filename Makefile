SFAQ="RasPi FAQ - Preguntas Frecuentas.docx"
S1="1 - Instalación y uso de Raspberry Pi.docx"
S2="2 - IOT y MQT.docx"
S3="3 - Programación: python y micropython.docx"
S4="4 - Arquitectura IOT.docx"

all: 1 2 3 4 FAQ

FAQ:
pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(SFAQ)  \
		Cabecera.md        \
		Cabecera_latex.md \
		z.raspi_faq.md

1:
	pandoc --pdf-engine=xelatex \
		--from=markdown \
		-V papersize:a4paper \
		--template=./LaTeX_ES.latex \
		--reference-doc=plantilla.docx \
		-o $(S1) \
		Cabecera.md        \
		Cabecera_latex.md \
		0.0.Proyecto.md \
		1.0.equipos.md \
		1.1.0.RaspberyPi.md \
		1.1.1.Raspberry_versiones.md \
		1.2.ESP32.md \
		1.3.kit.md \
		2.0.0.instalacion_raspberry.md \
		2.0.1.Documentacion_raspberry.md \
		2.1.0.Uso_raspberry.md \
		2.1.1.Arduino.md \
		2.1.2.ArduinoBlocks_v2.md \
		2.1.3.Scratch.md

2:
	pandoc --pdf-engine=xelatex       \
		-V papersize:a4paper        \
		--template=./LaTeX_ES.latex \
		--reference-doc=plantilla.docx \		
		-o $(S2) \
		Cabecera.md  \
		2.2.IOT.md\
		2.4.0.MQTT.md\
		2.4.1.mosquitto.md\
		2.4.2.Broquer_mqtt_externos.md\
		2.4.3.Herramientas.md
		
3:
	pandoc --pdf-engine=xelatex       \
		-V papersize:a4paper        \
		--template=./LaTeX_ES.latex \
		--reference-doc=plantilla.docx \		
		-o $(S3) \
		Cabecera.md        \
		Cabecera_latex.md \
		3.0.0.python.md \
		3.0.1.Thonny.md \
		3.1.0.python_variables.md \
		3.1.1.MQTT_python.md \
		3.1.2.MQTT_sensores.md \
		3.2.0.micropython.md \
		3.2.10.I2C.md \
		3.2.11.BME280.md \
		3.2.12.Oled.md \
		3.2.13.P.CO2.local.md \
		3.2.2.Instalacion_micropython.md \
		3.2.3.Uso_thonny.md \
		3.2.4.EntradaSalida.md \
		3.2.5.Ficheros_main_boot.md \
		3.2.6.ADC.md \
		3.2.7.sensores_dht.md \
		3.2.8.1.Adafruit_MQTT.md \
		3.2.8.wifi.md \
		3.2.9.0.MQTT_micropython.md

4:
	pandoc --pdf-engine=xelatex       \
		-V papersize:a4paper        \
		--template=./LaTeX_ES.latex \
		--reference-doc=plantilla.docx \
		-o $(S4) \
		Cabecera.md        \
		Cabecera_latex.md \
		4.0.arquitectura.md \
		4.1.docker.md \
		4.2.basedatos.md \
		4.3.0.domotica.md \
		4.3.1.DomoticaCasera.md \
		4.3.2.HomeAssistant.md \
		4.4.grafana.md \
		4.5.nodered.md
		