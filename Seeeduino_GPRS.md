---
title: Seeeduino GPRS
category: Arduino
bzurl: https://www.seeedstudio.com/Seeeduino-GPRS-p-1909.html
oldwikiname: Seeeduino_GPRS
prodimagename: seeeduino_gprs_cover.jpg
sku: 102010016
---

![](https://github.com/SeeedDocument/Seeeduino_GPRS/blob/master/images/seeeduino_gprs_cover.jpg?raw=true)

Seeeduino GPRS is a IoT panel, you can connect to the internet through GPRS wireless network with it. Making/answering voice calls and sending/receiving SMS messages are also supported. Meanwhile, Seeeduino GPRS supports FM radio function and bluetooth communication. Seeeduino GPRS is base on Atmage32U4 and SIM800H. Atmage32U4 is a microcontroller and it is compatible with Arduino. SIM800H support Quad-band 850/900/1800/1900MHz, it can transmit Voice, SMS and data information with low power consumption. SIM800H also brings some extra features like for example Bluetooth and FM radio. It is designed with power saving technique so that the current consumption is as low as 0.1mA in sleep mode. 


##Application Ideas

* Internet of Things  
* Smart House
* Wearable Designed
* DIY Phone
* Industrial

Here is some funny project for your reference.
|Arduino GPS/GSM Tracker|Arduino Phone 2.0|Arduino GPRS Weather Station|
|-------|-------|-------|
|![](http://www.instructables.com/file/FQ31270IA3RBCDI/)|![](http://www.instructables.com/file/FYPUI07IJQOBTKV/)|![](https://cdn.instructables.com/FA3/A69X/IMP61IX8/FA3A69XIMP61IX8.MEDIUM.jpg)|
|[Make it Now](http://www.instructables.com/id/Arduino-GPSGSM-Tracker/)|[Make it Now](http://www.instructables.com/id/ArduinoPhone-20-an-Open-Source-Mobile-Phone-Based-/)|[Make it Now](http://www.instructables.com/id/Arduino-GPRS-Weather-Station-Part-1/)|

##Features

* Compatible with standard Arduino Leonardo 
* Quad-Band 850/900/1800/1900MHz 
* Headset jack 
* Convenient external SIM card holder 
* Control via AT commands 
* Supports Bluetooth 
* Supports FM Radio 
* Current < 2A 
* Arduino Leonardob Bootloader 

##Specification

###SIM800H Model

|Parameter|Value|
|------------|------------|
|GPRS Model|SIM800H|
|Quad-Band|850/900/1800/1900MHz|
|GPRS multi-slot class|12/10|
|GPRS mobile station class|B|
|Standard GSM phase|2/2+|
|FM|76~109MHz|
|Bluetooth|Compliant with 3.0+EDR|
|Supply voltage range|3.4 ~ 4.4V|


###AVR Arduino Microcontroller

|Parameter|Value|
|------------|-------------|
|Microcontroller|ATmega32u4|
|Flash Memory|32KB|
|SRAM|2.5kB|
|EEPROM|1kB|
|Clock Speed|16MHz|
|Operating Voltage|5V|
|Digital I/O Pins|20|
|PWM Channels|7|
|Analog Input Channels|12|

#Hardware Overview

The images below show an overview of Seeeduino GPRS hardware features. The pin-out and alternate functions of various pins of Seeeduino GPRS are shown in the pin-out diagram. This could be used as a quick reference.

![](https://github.com/SeeedDocument/Seeeduino_GPRS/blob/master/images/seeeduino_gprs_hardware2.png?raw=true)

* **Power Switch**
Slide switch used to change the logic level and power output of the board to either 5V or 3.3V. 
Nowadays many new and great sensors are being develop to work with 3.3V, with other duino boards you would need to place a logic level converter between the board and these sensor(s), with the Seeeduino GPRS board all you have to do is slide the switch!
* **DC Input**
The DC Input allows your Seeeduino GPRS board to be powered from a wall adapter so that you can supply more power to your project if needed, for example when using DC motors or other high power devices. The DC input can be 9V-12V and peak current is 2A.
But there's a hardware bug in Seeeduino GPRS that you have to notice. When an external power input, there's very short 6V at the 5V pin, last about 2ms. **It is risk to destroy the device that connected to 5V.** So we recommend that don't use the DC Input to power the system. And we had considered to fix the bug already, but will not come out very soon.

* **Breakout for SIM800h**
You can debug Sim800h by this interface.

* **ICSP**
This is the ICSP connection for the ATMEGA32U4-MUR, it is located in the standard ICSP/SPI position for Arduino Uno, Due, Mega, and Leonardo compatible hardware (e.g. shields) that may use this connector. The SPI pins in this port: MISO, SCK, and MOSI, are also connected to digital pins 12, 13, and 11 respectively just like those of the Arduino Leonardo.

* **LED PWR2**
SIM800H Power Indication

* **LED STA**
Operating Status Indication

* **LED NET**
|Status|SIM800H Behavior|
|Off|SIM800H is not running|
|64ms on/800ms off|SIM800H not registered the network|
|64ms on/3000ms off|SIM800H registered the network|
|64ms on/300ms off|SIM800H communication is established|

##Getting Started

To start to play with the Seeeduino GPRS, a headphone and a SIM card are required.
![]()
![]()




##Resources

[Seeeduino GPRS Library on GitHub](https://github.com/Seeed-Studio/Seeeduino_GPRS)
Seeeduino GPRS Eagle file
Seeeduino GPRS PDF file
Seeeduino GPRS Firmware & Update Guide
SIM800 Series AT Command PDF



##FAQ


##Help us to make it better