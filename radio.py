import os
import time
import glob
import random
from gpiozero import MCP3008
from soxplayer import SoxPlayer

media_admin = glob.glob("/home/pi/tardis-radio/media/administrative/*.mp3")
media_1900 = glob.glob("/home/pi/tardis-radio/media/1900/*.mp3")
media_1910 = glob.glob("/home/pi/tardis-radio/media/1910/*.mp3")
media_1920 = glob.glob("/home/pi/tardis-radio/media/1920/*.mp3")
media_1930 = glob.glob("/home/pi/tardis-radio/media/1930/*.mp3")
media_1940 = glob.glob("/home/pi/tardis-radio/media/1940/*.mp3")
media_1950 = glob.glob("/home/pi/tardis-radio/media/1950/*.mp3")
media_1960 = glob.glob("/home/pi/tardis-radio/media/1960/*.mp3")
media_1970 = glob.glob("/home/pi/tardis-radio/media/1970/*.mp3")
media_1980 = glob.glob("/home/pi/tardis-radio/media/1980/*.mp3")
media_1990 = glob.glob("/home/pi/tardis-radio/media/1990/*.mp3")
media_grandpa_george = glob.glob("/home/pi/tardis-radio/media/grandpa-george/*.mp3")

# Globals
RADIO = SoxPlayer(media_admin[0])
CURRENT_CHANNEL_PLAYLIST = []
KNOB = MCP3008(channel=0)
HEARD = []

# get_channel() finds out where the pot is pointing to and returns the appropriate playlist name.
def get_channel():
    
    channels = 11
    radix = 1 / channels

    # get the average pot value after n readings. This reduces channels 'flipping' back and forth 
    # when tuned near the borders of two decades.
    n = 20    
    runningTotal = 0
    for i in range(n):
      runningTotal += KNOB.value
    averageValue = runningTotal / n

    if averageValue < (1 * radix):
        return media_1900
    if averageValue < (2 * radix):
        return media_1910
    if averageValue < (3 * radix):
        return media_1920
    if averageValue < (4 * radix):
        return media_1930
    if averageValue < (5 * radix):
        return media_1940
    if averageValue < (6 * radix):
        return media_1950
    if averageValue < (7 * radix):
        return media_1960
    if averageValue < (8 * radix):
        return media_1970
    if averageValue < (9 * radix):
        return media_1980
    if averageValue < (10 * radix):
        return media_1990
    if averageValue <= (11 * radix):
        return media_grandpa_george
    
def change_channel(newChannelPlaylist):
    os.system("sudo killall -9 sox")
    global CURRENT_CHANNEL_PLAYLIST
    global HEARD
    global RADIO
    
    # put all heard songs back
    CURRENT_CHANNEL_PLAYLIST.extend(HEARD)
    HEARD.clear()
    
    # set new channel
    CURRENT_CHANNEL_PLAYLIST = newChannelPlaylist
    
    # pick a song at random, move it to heard
    song = random.choice(CURRENT_CHANNEL_PLAYLIST)
    HEARD.append(song)
    CURRENT_CHANNEL_PLAYLIST.remove(song)
    
    # play the tuning sound (tardis) and then the song
    RADIO.tune_and_play(song)
    print('[TUNING] ' + str(song.split("/")[5]))
    
def play_next_song():
    global CURRENT_CHANNEL_PLAYLIST
    global HEARD
    global RADIO
    
    # pick a song at random and move it to the heard playlist
    song = random.choice(CURRENT_CHANNEL_PLAYLIST)
    HEARD.append(song)
    CURRENT_CHANNEL_PLAYLIST.remove(song)
    
    # play the song
    RADIO.play(song)

# Initialise
change_channel(get_channel())

while True:
    # change channel when appropriate
    if get_channel() != CURRENT_CHANNEL_PLAYLIST:
        change_channel(get_channel())
        
    # play next song when appropriate
    if not RADIO.is_playing():
        play_next_song()
    
    time.sleep(0.05)
