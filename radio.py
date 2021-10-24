#%%
import os
import time
import glob
import random
from gpiozero import MCP3008
from soxplayer import SoxPlayer

media_admin = glob.glob("/home/pi/radio/media/administrative/*.mp3")
media_1900 = glob.glob("/home/pi/radio/media/1900/*.mp3")
media_1910 = glob.glob("/home/pi/radio/media/1910/*.mp3")
media_1920 = glob.glob("/home/pi/radio/media/1920/*.mp3")
media_1930 = glob.glob("/home/pi/radio/media/1930/*.mp3")
media_1940 = glob.glob("/home/pi/radio/media/1940/*.mp3")
media_1950 = glob.glob("/home/pi/radio/media/1950/*.mp3")
media_1960 = glob.glob("/home/pi/radio/media/1960/*.mp3")
media_1970 = glob.glob("/home/pi/radio/media/1970/*.mp3")
media_1980 = glob.glob("/home/pi/radio/media/1980/*.mp3")
media_1990 = glob.glob("/home/pi/radio/media/1990/*.mp3")
media_grandpa_george = glob.glob("/home/pi/radio/media/grandpa-george/*.mp3")

# Globals
RADIO = SoxPlayer(media_admin[0])
CURRENT_CHANNEL_PLAYLIST = []
KNOB = MCP3008(channel=0)
HEARD = []

#%%

def get_channel():
    radix = 1 / 11
    if KNOB.value < (1 * radix):
        return media_1900
    if KNOB.value < (2 * radix):
        return media_1910
    if KNOB.value < (3 * radix):
        return media_1920
    if KNOB.value < (4 * radix):
        return media_1930
    if KNOB.value < (5 * radix):
        return media_1940
    if KNOB.value < (6 * radix):
        return media_1950
    if KNOB.value < (7 * radix):
        return media_1960
    if KNOB.value < (8 * radix):
        return media_1970
    if KNOB.value < (9 * radix):
        return media_1980
    if KNOB.value < (10 * radix):
        return media_1990
    if KNOB.value <= (11 * radix):
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
    
    if not CURRENT_CHANNEL_PLAYLIST:
        CURRENT_CHANNEL_PLAYLIST.extend(HEARD)
        HEARD.clear()
    
    # pick a song at random and move it to the heard playlist
    song = random.choice(CURRENT_CHANNEL_PLAYLIST)
    HEARD.append(song)
    CURRENT_CHANNEL_PLAYLIST.remove(song)
    
    # play the song
    RADIO.play(song)
    # print('[PLAYING] ' + str(song))

#%%
# Initialise
# CURRENT_CHANNEL_PLAYLIST = get_channel()
# change_channel(CURRENT_CHANNEL_PLAYLIST)
change_channel(get_channel())

while True:
    
    # change channel when appropriate
    if get_channel() != CURRENT_CHANNEL_PLAYLIST:
        change_channel(get_channel())
        time.sleep(0.1)
        
    # play next song when appropriate
    if not RADIO.is_playing():
        play_next_song()
    
    time.sleep(0.1)