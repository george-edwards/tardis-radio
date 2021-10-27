from soxplayer import SoxPlayer
import RPi.GPIO as GPIO
import subprocess
import os
from time import sleep
from datetime import datetime, timedelta

radio = SoxPlayer()
lowBatteryPin = 25

timeStart = datetime.now()

GPIO.setmode(GPIO.BCM)
GPIO.setup(lowBatteryPin, GPIO.IN)

while True:
    if not (GPIO.input(lowBatteryPin)):
        timeStop = datetime.now()
        duration = timeStop - timeStart
        os.system(f"echo '{str(duration)}\n' >> /home/pi/battery-duration.txt")
        os.system("sudo systemctl stop radio.service")
        radio.play("/home/pi/radio/media/administrative/lowbattery.mp3", True)
        os.system("sudo shutdown now")
        radio.play("/home/pi/radio/media/administrative/lowbattery.mp3", True)
        sleep(90)
    sleep(0.2)
