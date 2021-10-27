import os
import time
from math import floor
from gpiozero import MCP3008

volumePot = MCP3008(channel=1)
volumeValue = 0

while True:
    newValue = int(volumePot.value * 255)
    if not volumeValue-2 <= newValue < volumeValue+2:
        volumeValue = newValue
        os.system(f'amixer set Master {volumeValue}')
    time.sleep(0.1)