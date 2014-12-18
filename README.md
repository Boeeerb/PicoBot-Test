##Install

Enable SPI



sudo apt-get update

sudo apt-get install python-dev python-pip

sudo pip install spidev



Put both nrf24.py and server.py in a folder and sudo python server.py




##Aim:

The aim of the code is for the Pico bot to generate a random address (pipe), setup a recv pipe and then transmit its address to the Pi
The Pi will receive this on a fixed address, in the form of "NEW 12ab12ab12". Once it receives this it will reply to that address with the character "6".
Once the bot receives a "6" this turns on the red LED underneath





##Pico:

Mine have been modified with an RGB led underneath with

Red: D6
Green: D16 (A2)
Blue: D17 (A3)

White LED: D9


##Raspberry Pi:

(See Pinout.png)

Pi Pins - NRF Pins

17 - 2
19 - 6
20 - 1
21 - 7
22 - 3
23 - 5
24 - 4