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
BLACK = pygame.Color(0, 0, 0)

# Mathematical Definitions
#-------------------------------------------------------------------------------
def cosInterp (a, b, x):

    ft = pi * x
    f = (1 - cos(ft))*0.5

    ans = a*(1-f) + b*f
    
    return ans
  
def generateNoise (points):

    retval = list()
    
    for n in range(0, points):

        retval.append(res*random())

    return retval

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

def createNewPerlinNoiseGraph():

    surface.fill(WHITE)
    points = generateNoise(setpts)
    line = getLine(points)
    drawLine(line)
    pygame.display.update()

def getLine(points):

    retval = list()
    
    pxbtweenpts = res/(len(points) - 1)
    spaceperpx = 1.0/pxbtweenpts

    for n in range (0, len(points)):

        retval.append(points[n])

        if n < (len(points) - 1):
        
            for m in range (1, pxbtweenpts):
            
                newpointdx = m*spaceperpx
                newpointy = cosInterp(points[n], points[n+1], newpointdx)

                retval.append(int(newpointy))

    return retval

def drawLine(line):

    pxarr = pygame.surfarray.pixels2d(surface)
    prevpt = line[0]
    
    for n in range (0, len(line)):

        if prevpt < line[n] - 1:
            
            pxarr[n][prevpt + 1:line[n] + 1] = 0x000000
            
        elif line[n] < prevpt - 1:
            
            pxarr[n][line[n]:prevpt] = 0x000000
            
        else:
            
            pxarr[n][line[n]] = 0x000000
            
        prevpt = line[n]

setpts = 25
runApplication()
