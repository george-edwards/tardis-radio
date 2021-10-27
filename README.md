# tardis-radio
Time machine radio on the Raspberry Pi Zero

## Installation instructions

### Configure the Pi to use the Pimoroni DAC AMP SHIM.
Place the following in your SD card's /boot/config.txt
```
dtoverlay=hifiberry-dac
```

### Install git
```bash
sudo apt install git
```

### Clone repo
```bash
git clone https://github.com/george-edwards-code/tardis-radio.git
```
### enter directory
```bash
cd tardis-radio
```

### Run installer script
```bash
sudo ./install.sh
```
