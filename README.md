# tardis-radio
Time machine radio on the Raspberry Pi Zero

## Buy the hardware
* [Raspberry Pi Zero W 2](https://www.google.com/search?q=raspberry+pi+zero+w+2&tbm=shop)
* [Adafruit PowerBoost 1000C](https://www.google.com/search?q=adafruit+powerboost+1000c&tbm=shop)
* [Proto Board for RPi-Zero](https://www.google.com/search?tbm=shop&q=Raspberry+Pi+Zero+Proto+Board)
* [Tuning Potentiometer - PTV09A-4025F-B103](https://www.google.com/search?tbm=shop&q=PTV09A-4025F-B103)
* [On/Off switch (DPDT on-on)](https://www.google.com/search?tbm=shop&q=DPDT+switch+on-on)
* [Enclosure (NR-3013 Radio)](https://www.google.com/search?tbm=shop&q=NR-3013+radio)

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
```bash
sudo apt install git
```

### Clone repo
```bash
git clone https://github.com/byte-rider/tardis-radio.git
```
### enter directory
```bash
cd tardis-radio
```

### Run installer script
```bash
sudo ./install.sh
```
