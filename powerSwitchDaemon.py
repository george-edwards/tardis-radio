import RPi.GPIO as GPIO
import os
from time import sleep

powerSwitchPin = 22
keepAlivePin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(powerSwitchPin, GPIO.IN)
GPIO.setup(keepAlivePin, GPIO.OUT)

while True:
    GPIO.output(keepAlivePin, GPIO.HIGH)
    if not GPIO.input(powerSwitchPin):
        os.system("sudo systemctl stop tardis-radio.service")
        os.system("play -q /home/pi/tardis-radio/media/administrative/lowbattery.mp3 2>/dev/null")
        os.system("sudo poweroff")
        sleep(30)
    sleep(0.05)
