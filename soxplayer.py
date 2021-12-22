import os
import subprocess
import time

class SoxPlayer:
    '''
    A wrapper for SoX program. SoX is invoked through shell commands spawned by Python subprocesses
    requirements:
        sudo apt install sox libsox-fmt-all bc
    '''
    currentlyPlayingProcess = None
    tardisPath = None
    
    # pass the tardis mp3's path through upon instantiation
    def __init__(self, tardisPath = None) -> None:
        if tardisPath != None:
            self.tardisPath = tardisPath
        pass
    
    def play(self, songPath, blocking = False):
        self.stop()
        
        if blocking:
            os.system(f"AUDIODEV=hw:1,0 /usr/bin/play -q '{songPath}' 2>/dev/null")
        else:
            self.currentlyPlayingProcess = subprocess.Popen(['sox', '-V0', '-q', songPath, '-d'])
    
    def tune_and_play(self, songPath, percentage = 0.5):
        '''
        stop the current song, play the tardis sound while fading-in the new song.
        The new song will begin @percentage of the way through (function argument)
        '''
        
        # kill old song
        self.stop()
        
        # find the starting position of the song using the length of the song * percentage. The length is got by soxi and the calculation by bc
        songStartingPosition = subprocess.check_output(f"echo $(soxi -D \"{songPath}\")*{percentage}/1 | bc", shell=True, universal_newlines=True)
        
        # play the tardis and the new song together, but fade the new song in allowing time for the tardis to be heard on its own
        cmd1 = subprocess.Popen(['sox', '-V0', '-q', songPath, '-p', 'trim', f'{int(songStartingPosition)}', 'fade', '5'], stdout=subprocess.PIPE)
        self.currentlyPlayingProcess = subprocess.Popen(['sox', '-V0', '-q', '-', '-m', self.tardisPath, '-d'], stdin=cmd1.stdout)
        
    def stop(self):
        os.system("sudo killall -9 sox")
    
    def is_playing(self):
        if self.currentlyPlayingProcess == None or self.currentlyPlayingProcess.poll() != None:
            return False
        else:
            return True