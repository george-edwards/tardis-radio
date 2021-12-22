from soxplayer import SoxPlayer
import RPi.GPIO as GPIO
import os
from time import sleep

radio = SoxPlayer()
lowBatteryPin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(lowBatteryPin, GPIO.IN)

while True:
    if not (GPIO.input(lowBatteryPin)):
        os.system("sudo systemctl stop radio.service")
        radio.play("/home/pi/tardis-radio/media/administrative/lowbattery.mp3", True)
        os.system("sudo shutdown now")
        sleep(90)
    sleep(0.5)