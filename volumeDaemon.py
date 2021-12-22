import os
import time
from gpiozero import MCP3008

volumePot = MCP3008(channel=1)
volumeValue = 0

while True:
    # To invert the volume control comment out the other one of the two lines below.
    # By invert I mean if the volume goes down rather than up while rotating clockwise.
    
    #newValue = int(volumePot.value) * 255)
    newValue = int((1 - volumePot.value) * 255)
    
    # the threashold below can be increased depending on how 'jumpy' your volume pot is
    if not volumeValue-1 <= newValue < volumeValue+1:
        volumeValue = newValue
        os.system(f'amixer set Master {volumeValue}')
    time.sleep(0.05)