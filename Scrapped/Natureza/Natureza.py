"""
The main game, contains useful constants meant to be used throughout
the program
"""
from sfml import *

def MAPSIZE():
    return 45 #tiles
def TILESIZE():
    return 80 #pixels
def VIDEOMODE():
    return VideoMode(800, 640)
def FPS():
    return 30 #frames per second
def MINUTES_IN_A_GAMEDAY():
    return 20 #minutes
def FRAMES_IN_A_GAMEDAY():
    return FPS()*MINUTES_IN_A_GAMEDAY()*60 #seconds
def TREE_MATURATION_TIME():
    return SECONDS_IN_A_GAMEDAY()*60 #ticks at 1 fertility
