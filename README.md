# tardis-radio
Time machine radio on the Raspberry Pi Zero

YouTube:  
<a href="http://www.youtube.com/watch?feature=player_embedded&v=eJmE6S1rkvI
" target="_blank"><img src="http://img.youtube.com/vi/eJmE6S1rkvI/0.jpg" 
alt="A video showing a `time machine radio` made possible by a Raspberry Pi Zero" width="320" height="240" border="10" /></a>

## Buy the hardware
* [Raspberry Pi Zero W 2](https://www.google.com/search?q=raspberry+pi+zero+w+2&tbm=shop)
* [Pimoroni Audio Amp SHIM](https://www.google.com/search?q=Pimoroni+Audio+Amp+SHIM&tbm=shop)
* [Adafruit PowerBoost 1000C](https://www.google.com/search?q=adafruit+powerboost+1000c&tbm=shop)
* [Proto Board for RPi-Zero](https://www.google.com/search?tbm=shop&q=Raspberry+Pi+Zero+Proto+Board)
* [Tuning Potentiometer - PTV09A-4025F-B103](https://www.google.com/search?tbm=shop&q=PTV09A-4025F-B103)
* [On/Off switch (DPDT on-on)](https://www.google.com/search?tbm=shop&q=DPDT+switch+on-on)
* [Enclosure (NR-3013 Radio)](https://www.google.com/search?tbm=shop&q=NR-3013+radio)
* [Micro-USB mount](https://www.google.com/search?q=Micro+USB+B+Jack+to+USB+A+Plug+Round+Panel+Mount+Adapter&tbm=shop)  
  * [the exact one I bought](https://core-electronics.com.au/micro-usb-b-jack-to-usb-a-plug-round-panel-mount-adapter.html)

## Software Installation instructions

### Enable the DAC AMP SHIM
place the following in your SD card's /boot/config.txt
```
dtoverlay=hifiberry-dac
```

enable the SPI Interface through the raspberry pi's config
```
sudo raspi-config

# Interface > SPI > Enable
```

### Install git
```
sudo apt install git
```

### Clone repo
```
git clone https://github.com/byte-rider/tardis-radio.git
```
### Run installer script
```
cd tardis-radio
sudo ./install.sh
```

## Hardware modifications
stub

## Wiring diagrams
stub