import pygame, sys, numpy
from pygame.locals import*
from math import*
from random import random

# Pygame Initation
#-------------------------------------------------------------------------------
pygame.init()
res = 512
fpsClock = pygame.time.Clock()
FPS = 30
surface = pygame.display.set_mode((res, res))

# Colors
#-------------------------------------------------------------------------------
WHITE = pygame.Color(255, 255, 255)
STD_GREY = pygame.Color(128, 128, 128)
BLACK = pygame.Color(0, 0, 0)

def createNewPerlinNoiseGraph():

    surface.fill(WHITE)
    points = generateNoise()
    smooth()
    pygame.display.update()

def generateNoise():

    pxarr = pygame.surfarray.pixels2d(surface)
    for n in range (0, res):
        for m in range (0, res):
            randGrey = toGreyHex(int(0xFF*random()))
            pxarr[n][m] = randGrey

def toGreyHex (num):
    
    return num*0x10000 + num*0x100 + num

def to8bitGrey (num):

    return num%0x0000FF

def smooth():

    pxarr = pygame.surfarray.pixels2d(surface)
    for n in range (1, res - 1):
        for m in range (1, res - 1):
            #corners = (to8bitGrey(pxarr[n-1][m-1]) + to8bitGrey(pxarr[n+1][m-1]) + to8bitGrey(pxarr[n-1][m+1]) + to8bitGrey(pxarr[n+1][m+1]))/32
            sides = 3*(to8bitGrey(pxarr[n][m+1]) + to8bitGrey(pxarr[n+1][m]) + to8bitGrey(pxarr[n-1][m]) + to8bitGrey(pxarr[n][m-1]))/16
            center = to8bitGrey(pxarr[n][m])/4

            pxarr[n][m] = toGreyHex(sides + center)

def runApplication():

    while True:

        if processCommands():
            
            createNewPerlinNoiseGraph()

def processCommands():
    
    for event in pygame.event.get():
        
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            
            return True

        else:

            return False
    
runApplication()
