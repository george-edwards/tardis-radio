from soxplayer import SoxPlayer
import RPi.GPIO as GPIO
import subprocess
import os
from time import sleep

radio = SoxPlayer()
powerSwitchPin = 23
keepAlivePin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(powerSwitchPin, GPIO.IN)
GPIO.setup(keepAlivePin, GPIO.OUT)

while True:
    GPIO.output(keepAlivePin, GPIO.HIGH)
    if not (GPIO.input(powerSwitchPin)):
        os.system("sudo systemctl stop radio.service")
        radio.play("/home/pi/tardis-radio/media/administrative/lowbattery.mp3", True)
        os.system("sudo shutdown now")
        radio.play("/home/pi/tardis-radio/media/administrative/lowbattery.mp3", True)
        sleep(90)
    sleep(0.2)
