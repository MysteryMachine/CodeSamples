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

    points = generateNoise(32, 0.1)
    smooth(1)
    points = generateNoise(16, 0.1)
    smooth(1)
    points = generateNoise(8, 0.1)
    smooth(1)
    points = generateNoise(4, 0.1)
    smooth(1)
    points = generateNoise(2, 0.1)
    smooth(1)
    points = generateNoise(1, 0.1)
    smooth(1)
    print("done")
    pygame.display.update()

#freq <= res
#0 < amp <= 1

def generateNoise(period, amp, power = True):

    pxarr = pygame.surfarray.pixels3d(surface)
    for n in range (0, (res/period)):
        for m in range (0, (res/period)):
            if not power:
                dcolor = amp*(0.5 - random())*0xFF/2
            else:
                dcolor = amp*((pow(16, 2*(random()))))
            for j in range (0, period):
                for k in range (0, period):
                    if pxarr[period*n + j][period*m+k][0] + dcolor >= 255:
                        pxarr[period*n + j, period*m+k, :] = 255
                    else: 
                        pxarr[period*n + j, period*m + k, :] += dcolor
                    
def smooth(smoothlevel):
    
    pxarr = pygame.surfarray.pixels3d(surface)

    for z in range(0, smoothlevel):
        for n in range (1, res - 1):
            for m in range (1, res - 1):
                sides = 3*(int(pxarr[n][m+1][0]) + int(pxarr[n+1][m][0]) + int(pxarr[n-1][m][0]) + int(pxarr[n][m-1][0]))/16
                center = pxarr[n][m][0]/8
                pxarr[n][m][:] = sides + center

def runApplication():

    while True:

        if processCommands():
            
            createNewPerlinNoiseGraph()

def processCommands():
    
    for event in pygame.event.get():
        
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN and event.key == K_RETURN:
            
            return True

        else:

            return False
    
runApplication()
