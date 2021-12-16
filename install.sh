#!/bin/bash -v
echo "installing pre-requisites"
sudo apt install sox libsox-fmt-all bc -y

echo "installing systemd daemons"
sudo cp systemd-files/* /lib/systemd/system/
sudo systemctl daemon-reload
#sudo systemctl enable low-power-daemon.service
#sudo systemctl enable power-switch-daemon.service
sudo systemctl enable radio.service
sudo systemctl enable volume-daemon.service

echo "configuring sound device for soft-volume"
cp .asoundrc /home/pi/
