#!/bin/bash -v
echo "installing pre-requisites"
sudo apt install sox libsox-fmt-all bc -y

echo "installing systemd daemons"
sudo cp systemd-files/* /lib/systemd/system/
sudo systemctl daemon-reload
#sudo systemctl enable tardis-radio-low-power-daemon.service
#sudo systemctl enable tardis-radio-power-switch-daemon.service
sudo systemctl enable tardis-radio.service
sudo systemctl enable tardis-radio-volume-daemon.service

echo "configuring sound device for soft-volume"
cp .asoundrc /home/pi/
