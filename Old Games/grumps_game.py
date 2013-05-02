# This game was created as part of a one game a month challenge, the art assets
# are available upon request, but as of now it is not published anywhere, as the
# the game itself is not very fun. Please ask me about what improvements I would
# make if I were to design this again, now that I have more experience. In general
# I'd say I hard coded too much in this game.

import pygame, sys, numpy, copy
from pygame.locals import*
from math import*
from random import random

# Main game class, initates important game variables, runs the main game loops, handles
# rendering objects and game logic
# ----------
class grumpsGame:
    def __init__(this):        
        # Pygame Initation
        # ----------
        pygame.init()
        this.resX, this.resY = 1024, 600
        this.fpsClock = pygame.time.Clock()
        this.FPS = 30
        this.surface = pygame.display.set_mode((this.resX, this.resY))

        # Colors
        # ----------
        this.WHITE = pygame.Color(255, 255, 255)
        this.STD_GREY = pygame.Color(128, 128, 128)
        this.BLACK = pygame.Color(0, 0, 0)
        this.DRKOJ = pygame.Color(230, 110, 49)
        this.LGTOJ = pygame.Color(243, 164, 72)
        this.DRKBLU = pygame.Color(122, 141, 219)
        this.CLRKEY = pygame.Color(122, 141, 218)
        this.LGTBLU = pygame.Color(167, 230, 248)

        # Loading
        # ----------
        this.music = pygame.mixer.music.load('witl.mp3')    

        # Logic Variables
        # ----------

        # gameEntities requires a bit of explaining, the lists will contain objects
        # for rendering, and will be rendered from smallest to greatest, thus, based on where
        # objects are on each list, they will have a priority for rendering and for their logic
        # this lets me avoid sorting the lists everytime
        # As of now:
        # background entities should be assigned to gameEntities[0]
        # shots fired from either side should be assigned to gameEntities[1]
        # enemies should be assigned to gameEntities[2]
        # the player will soley occupy the final list
        this.gameEntities = [list(), list(), list(), list(), list()]
        
        this.mX, this.mY = 0, 0

        # These three variables are used to initalize and continue the logic of the rectangles at
        # the top of the screen
        this.rectCount = 0
        this.topRectSize = [32, 16]
        this.ojPick = True

        # Checks to see if we're still displaying the menu
        this.isMenu = True

        pygame.mixer.music.play(-1)

        
    # startScreen()
    # Adds the initial game menu to the gameEntities list so it can render
    # graphics and do menu logic
    # ----------
    def startScreen(this):
        menu.bg = pygame.image.load('startscreen.png').convert()
        menu.select = pygame.image.load('start1.png').convert_alpha()
        menu.selectHilite = pygame.image.load('start2.png').convert_alpha()
        this.gameEntities[0].append(menu(this))

    # initGame()
    # Loads the rest of the game logic
    # ----------
    def initGame(this):
        # Cleanup
        # ----------
        this.isMenu = False
        this.gameEntities[0][0].delete = True
        this.surface.fill(this.BLACK)

        # Loading
        # ----------    
        dankeyKang.dankeyKangPic = pygame.image.load('kang.png').convert()
        dankeyKang.dankeyKangPic.set_colorkey(this.CLRKEY)
        dankeyKang.notDankeyKangPic = pygame.image.load('luigi.png').convert()
        dankeyKang.notDankeyKangPic.set_colorkey(this.CLRKEY)
        miku.miku1 = pygame.image.load('miku1.png').convert()
        miku.miku1.set_colorkey(this.CLRKEY)
        miku.miku2 = pygame.image.load('miku2.png').convert()
        miku.miku2.set_colorkey(this.CLRKEY)
        bulletEntity.shotE = pygame.image.load('shote.png').convert()
        bulletEntity.shotE.set_colorkey(this.CLRKEY)
        bulletEntity.shotP = pygame.image.load('shotg.png').convert()
        bulletEntity.shotP.set_colorkey(this.CLRKEY)
        entity.plosion = pygame.image.load('plosion.png').convert()
        entity.plosion.set_colorkey(this.CLRKEY)

        # Logic
        # ----------
        this.gameEntities[3].append(playerEntity(this))

        this.player = this.gameEntities[3][0]

        this.spawn = spawner(30, 1500, this)

    
        this.generateInitialRects()
        pygame.mouse.set_visible(False)
        
    # startGame()
    # Loads the start screen, then calls input and logic checks, updates the screen
    # and ticks the clock
    # ---------
    def startGame(this):

        this.startScreen()
        
        while True:
            this.updateScreen()
        
            this.checkInputs()
            this.updateGameLogic()
        
            this.fpsClock.tick(this.FPS)
            
    # updateGameLogic()
    # First deletes any entities that need deleting
    # Handles the creation of any new entities second, according to the priority noted in the above note
    # about gameEntities, then it ticks them in thaat same orderinitGame
    # ----------
    def updateGameLogic(this):
        if not this.isMenu:    
            this.generateEdgeRects()
            this.spawn.generate()
            this.handleAllCollisions()
        
        for n in range (0, len(this.gameEntities)):
            for item in this.gameEntities[n]:
                if item.delete or item.tick():
                    this.gameEntities[n].remove(item)

    # handleAllCollisions()
    # Calls all other collision functions
    # ----------
    def handleAllCollisions(this):
        this.checkEnemyCollisionsWithAll()
        this.checkShotCollisionsWithAll()
        this.checkPlayerCollisionsWithAll()

    # checkCollision()
    # Checks collision between a rectangle and checks for collisions with all
    # Rects in the gameEntities list for the checkRange provided
    # ----------
    def checkCollision(this, item, checkRange):

        rect0 = Rect(item.X, item.Y, item.width, item.height)
        for n in checkRange:
            for item2 in this.gameEntities[n]:
                if item2 is not item:
                    rect1 = Rect(item2.X, item2.Y, item2.width, item2.height)
                    if rect0.colliderect(rect1):
                        item.collide(item2)
    # chckCollisionPlayer()
    # Checks collision of a Rect with the rects of the players
    # ----------
    def checkCollisionPlayer(this, item):
        rect0 = Rect(item.X, item.Y, item.width, item.height)
        rectA = Rect(this.player.arinRect[0] + this.player.X - this.player.grumpsCenter[0],
                     this.player.arinRect[1] + this.player.Y - this.player.grumpsCenter[1],
                     this.player.arinRect[2],
                     this.player.arinRect[3])
        rectJ = Rect(this.player.jonRect[0] + this.player.X - this.player.grumpsCenter[0],
                     this.player.jonRect[1] + this.player.Y - this.player.grumpsCenter[1],
                     this.player.jonRect[2],
                     this.player.jonRect[3])

        if rect0.colliderect(rectA) or rect0.colliderect(rectJ):
            this.player.collide(item)

            
    # checkEnemyCollisionsWithAll()
    # For every enemy, check collisions with all shots
    # ----------
    def checkEnemyCollisionsWithAll(this):
        for item in this.gameEntities[2]:
            this.checkCollision(item, range(1, 2))

    # checkShotCollisionsWithAll
    # Check for shot collisions with enemies and the players
    # ----------
    def checkShotCollisionsWithAll(this):
        for item in this.gameEntities[1]:
            this.checkCollision(item, range(2, 3))
            this.checkCollisionPlayer(item)
            
    # checkPlayerCollisionsWithAll
    # check player collisions with shots and the enemy
    # ----------
    def checkPlayerCollisionsWithAll(this):
        for item in this.gameEntities[1]:
            this.checkCollisionPlayer(item)
        for item in this.gameEntities[2]:
            this.checkCollisionPlayer(item)
            
    # generateEdgeRects()        
    # Every 32 ticks, generate a new rectangle of alternating color on top and bottom
    # ----------
    def generateEdgeRects(this):
        if this.rectCount == 0:
            chosenClr = 0
            
            if this.ojPick:
                chosenClr = this.LGTOJ
                
            else:
                chosenClr = this.DRKOJ

            this.ojPick = not this.ojPick
        
            this.gameEntities[0].append(entityRectOJ(this.resX, 0, 0, this.topRectSize[0], this.topRectSize[1], chosenClr))
            this.gameEntities[0].append(entityRectOJ(this.resX, this.resY - this.topRectSize[1], 0,this.topRectSize[0], this.topRectSize[1], chosenClr))
            this.rectCount += 1
        
        elif this.rectCount > 0:
        
            if this.rectCount == 31:
                this.rectCount = 0
            else:
                this.rectCount += 1
        
    # generateInitialRects()
    # Generates the inital OJ rects at the top, draws them to the defined dimensions, draws them on top and bottom, alternating colors
    # Then draws the big blue field in the middle of the game
    # ----------
    def generateInitialRects(this):
        for n in range(0, this.resX, this.topRectSize[0]):

            chosenClr = 0
            
            if this.ojPick:
                chosenClr = this.LGTOJ
                
            else:
                chosenClr = this.DRKOJ

            this.ojPick = not this.ojPick
            
            this.gameEntities[0].append(entityRectOJ(n , 0, this.topRectSize[0], this.topRectSize[0], this.topRectSize[1], chosenClr))
            this.gameEntities[0].append(entityRectOJ(n, this.resY - this.topRectSize[1], this.topRectSize[0], this.topRectSize[0], this.topRectSize[1], chosenClr))

        this.gameEntities[4].append(entityRect(0, this.topRectSize[1], this.resX, this.resY - 2*this.topRectSize[1], this.DRKBLU))
        this.gameEntities[4][0].delete = False
        
    # updateScreen()
    # Draws all the entities in the gameEntities 2D list in priority order
    # ----------
    def updateScreen(this):
        for n in range (len(this.gameEntities) - 1, -1, -1):
            for item in this.gameEntities[n]:
                item.draw(this.surface)
        
        pygame.display.update()

    # checkInputs()
    # self-explanatory, no tricks in this
    # ----------
    def checkInputs(this):
    
        for event in pygame.event.get():
        
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                
                pygame.quit()
                sys.exit()

            else:
                this.processEvent(event)

    # processEvent()
    # Checks mouse motion, mouse up, mouse down and calls the appropriate function
    # ----------
    def processEvent(this, event):

        if event.type == MOUSEMOTION:
            this.processMouseMove(event)

        if event.type == MOUSEBUTTONDOWN:
            this.processClick(event)

        if event.type == MOUSEBUTTONUP:
            this.finishClick(event)
            
    # processClick
    # If we're in menu and over the start button, start the game
    # if not, if the player can shoot, mark where the click started
    # ----------
    def processClick(this, event):
        if not this.isMenu: 
            if event.button == 1 and this.player.mArinTicks == this.player.fireSpeed:
                this.player.storedXArin = this.player.X
                this.player.storedYArin = this.player.Y
            if event.button == 3 and this.player.mJonTicks == this.player.fireSpeed:
                this.player.storedXJon = this.player.X
                this.player.storedYJon = this.player.Y

        else:
            if this.gameEntities[0][0].hilite:
                this.initGame()

    # finishClick()
    # If not in the menu, and the player can fire, then fire
    # ----------
    def finishClick(this, event):
        if not this.isMenu: 
            if event.button == 1 and this.player.mArinTicks == this.player.fireSpeed:
                this.player.mArinFire = True
            if event.button == 3 and this.player.mJonTicks == this.player.fireSpeed:
                this.player.mJonFire = True

    # processMouseMove()
    # Store where the mouse is, if not in the menu, don't let it go up far enough
    # so that it leaves where the playable screen is
    # ----------
    def processMouseMove(this, event):
        x, y = event.pos


        if not this.isMenu:  
            if x < this.player.grumpsCenter[0]:
                this.mX = this.player.grumpsCenter[0]
                pygame.mouse.set_pos(this.player.grumpsCenter[0], y)
            
            elif x > this.resX - this.player.grumpsImgSize[0] + this.player.grumpsCenter[0]:
                this.mX = this.resX - this.player.grumpsImgSize[0] + this.player.grumpsCenter[0]
                pygame.mouse.set_pos( this.resX - this.player.grumpsImgSize[0] + this.player.grumpsCenter[0], y)
            
            else:
                this.mX = x
            
            if y < this.player.grumpsCenter[1] + this.topRectSize[1]:
                this.mY = this.player.grumpsCenter[1] + this.topRectSize[1]
                pygame.mouse.set_pos(this.mX, this.player.grumpsCenter[1] + this.topRectSize[1])
            
            elif y > this.resY - this.gameEntities[3][0].grumpsImgSize[1] + this.player.grumpsCenter[1] - this.topRectSize[1]:
                this.mY = this.resY -  this.player.grumpsImgSize[1] + this.player.grumpsCenter[1] - this.topRectSize[1]
                pygame.mouse.set_pos(this.mX, this.resY - this.player.grumpsImgSize[1] + this.player.grumpsCenter[1] - this.topRectSize[1])
            
            else:
               this.mY = y

        else:
            this.mY, this.mX = y, x
        
# entity
# The parent class to all other entities, the methods within the entities contain their
# game logic and their rendering logic, tick() is the game logic, draw() is the rendering
# logic
# ----------
class entity:

    plosion = 0
    plosionSize = (160, 160)
    
    def __init__(this, X, Y):
        
        this.X = X
        this.Y = Y
        this.delete = True
        this.collided = False

    # tick()
    # If return whether or not entity ought to be removed of gameEntities list
    # False means do not remove, True means remove
    # ----------
    def tick(this):
        return this.delete
    
    def draw(this, surface):
        None

    def collide(this, item):
        None
    
# entityRect
# This class will be used for one single draw, used for delta updates
# ----------
class entityRect(entity):
    
    def __init__(this, X, Y, width, height, color):
        
        this.X = X
        this.Y = Y
        this.height = height
        this.width = width
        this.color = color
        this.delete = False
        
    def draw (this, surface):
        
        pygame.draw.rect(surface, this.color, pygame.Rect(this.X, this.Y, this.width, this.height))

# entityRectOJ
# Used for OJ rectangles at top and bottom of the screen, on tick, move rect to left, if at left size of screen, reduce size
# If size is zero, mark for deletion
# ----------
class entityRectOJ(entityRect):
    def __init__(this, X, Y, width, maxwidth, height, color):
        
        this.X = X
        this.Y = Y
        this.height = height
        this.width = width
        this.maxwidth = maxwidth
        this.color = color
        this.delete = False
      
    def draw (this, surface):
        pygame.draw.rect(surface, this.color, pygame.Rect(this.X, this.Y, this.width, this.height))

    def tick(this):
        if this.width < this.maxwidth:
            this.width += 1
        
        if(this.X > 0):
            this.X -= 1    

        elif(this.X == 0 and this.width > 0):
            this.width -= 1

        else:
            this.delete = True
        
        return this.delete
    
# playerEntity
# Holds all the logic regarding the player
# ----------
class playerEntity(entity):
    def __init__(this, game):
        # Load images
        # -----------
        this.grump = pygame.image.load('grumps.png').convert()
        this.grump.set_colorkey(game.CLRKEY)
        this.mArin = pygame.image.load('arinm.png').convert()
        this.mJon = pygame.image.load('jonm.png').convert()

        # Locational and vector quants
        # ----------
        this.X = 0
        this.Y = 0
        this.dXn = 300
        
        this.shotTypeArin = "single"
        this.shotTypeJon = "single"
        this.dmgArin = 1
        this.dmgJon = 1

        this.storedXArin = 0
        this.storedYArin = 0
        this.storedXJon = 0
        this.storedYJon = 0
        
        # Geometry
        # -----------
        this.grumpsCenter = (182, 130)
        this.arinRect = (35, 21, 160, 145)
        this.jonRect = (155, 78, 160, 149)
        this.grumpsImgSize = (353, 244)
        this.mArinLoc = (125, 84)
        this.mJonLoc = (235, 127)

        # Logic
        # -----------
        this.mJonFire = False
        this.mArinFire = False
        this.mArinTicks = 0
        this.mJonTicks = 0
        this.fireSpeed = 3
        this.mouthOpenTime = -20
        this.collided = False
        this.invulnTime = game.FPS * 3
        this.wait = 0
        this.life = 3
        this.damp = 6.0
        this.delete = False
        this.isHostile = False

        # Pointers
        # -----------
        this.game = game

    # tick()
    # If firing, open the mouth and count how long it'll stay open
    # If hit, count how long you reamin invulnerable
    # Call the fire function
    # ----------
    def tick(this):
        
        this.X , this.Y = this.game.mX, this.game.mY

        if this.mArinFire:
            this.mArinTicks = this.mouthOpenTime
        elif this.mArinTicks < this.fireSpeed:
            this.mArinTicks+=1

        if this.mJonFire:
            this.mJonTicks = this.mouthOpenTime
        elif this.mJonTicks < this.fireSpeed:
            this.mJonTicks+=1

        if this.wait == this.invulnTime:
            this.wait = 0

        if this.wait > 0:
            this.wait+=1

        this.fire()

    # fire()
    # Calculates the vector used for curving the shot, adds the shot to the entities
    # If not firing, do nothing
    # ----------
    def fire(this):
        
        if this.mArinFire:
            dX = this.X - this.storedXArin
            dY = this.Y - this.storedYArin

            if -1*dX >= this.dXn*.5:
                dX = 0.5*this.dXn
            if dY >= this.dXn:
                dY = this.dXn
            elif -dY >= this.dXn:
                dY = -this.dXn
            
            if this.shotTypeArin == "single":
                this.game.gameEntities[1].append(bulletEntity(this.mArinLoc[0] + this.X - this.grumpsCenter[0],
                                                                           this.mArinLoc[1] + this.Y - this.grumpsCenter[1],
                                                              (dX/this.damp + this.dXn, dY), False, this.dmgArin, this.game.FPS))
                this.mArinFire = False
        if this.mJonFire:
            dX = this.X - this.storedXJon
            dY = this.Y - this.storedYJon

            if -1*dX >= this.dXn*.5:
                dX = 0.5*this.dXn
            if dY >= this.dXn:
                dY = this.dXn
            elif -dY >= this.dXn:
                dY = -this.dXn
            
            if this.shotTypeJon == "single":
                this.game.gameEntities[1].append(bulletEntity(this.mJonLoc[0] + this.X - this.grumpsCenter[0],
                                                                          this.mJonLoc[1] + this.Y - this.grumpsCenter[1],
                                                              (dX/this.damp + this.dXn, dY), False, this.dmgJon, this.game.FPS))
                this.mJonFire = False
    # draw()
    # Draw the players and the mouths, don't draw them if the "just hit" wait is odd
    # ----------
    def draw(this, surface):

        if this.wait%2 == 0:
            surface.blit(this.grump, (this.X - this.grumpsCenter[0], this.Y - this.grumpsCenter[1]))

            if this.mJonTicks < 0:
                surface.blit(this.mJon, (this.mJonLoc[0] + this.X - this.grumpsCenter[0], this.mJonLoc[1] + this.Y - this.grumpsCenter[1]))

            if this.mArinTicks < 0:
                surface.blit(this.mArin, (this.mArinLoc[0] + this.X - this.grumpsCenter[0], this.mArinLoc[1] + this.Y - this.grumpsCenter[1]))

    # collide()
    # lower the player's life, quit game if out of lives
    # ----------
    def collide(this, item):
        if item.isHostile and this.wait == 0:
            this.life -= item.dmg
            this.wait = 1

        if this.life == 0:
            pygame.quit()
            sys.exit()
            
# bulletEntity
# handles logic for all the bullets
# ----------
class bulletEntity(entity):
    # Used for graphics
    shotE, shotP = 0, 0   
    def __init__(this, X, Y, vector, isHostile, dmg, gameFPS):

        # Position
        # ----------
        this.X = X
        this.Y = Y

        # Assigns image
        # ----------
        if isHostile:
            this.pic = bulletEntity.shotE.copy()
            
        if not isHostile:
            this.pic = bulletEntity.shotP.copy()
            
        # Figures vector ou
        # ----------
        this.dX = (vector[0])/gameFPS
        this.dY = (vector[1])/gameFPS

        # Logic
        # ----------
        this.size = (25, 26)

        this.isHostile = isHostile

        this.dmg = dmg

        this.delete = False
        this.collided = False
        this.collideCount = 5

        this.width = this.size[0]
        this.height = this.size[1]
        
    # tick()
    # Checks to see if the bullet should be deleted, and if its collided
    # wait until its time to be delted
    # ----------
    def tick(this):

        this.X+=this.dX
        this.Y+=this.dY

        if this.collided and this.collideCount == 0:
            this.delete = True

        elif this.collided:
            this.collideCount-=1

        if this.X < -this.size[0] or this.Y < -this.size[1]:
            this.delete = True
            
    # tick()
    # Draw bullet, if drawn, make less visible
    # ----------
    def draw(this, surface):
        if this.collided:
            this.pic.set_alpha(51*this.collideCount)
            
        surface.blit(this.pic, (this.X, this.Y))

    # collide()
    # checks collision
    # ----------
    def collide(this, item):
        if this.isHostile and not item.isHostile:
            this.collided = True
        if not this.isHostile and item.isHostile:
            this.collided = True

# dankeyKang
# Handles all logic on luigi and donkey kong enemies, putting them together is less efficient and logical
# but I made it as a joke for myself, because this is my own personal code
# ----------
class dankeyKang(entity):
    # Image loading vars
    dankeyKangPic = 0
    notDankeyKangPic = 0
    kangDim = (75, 87)
    notKangDim = (98, 112)

    def __init__(this, X, Y, vector, isKang, gameFPS):

        # Position
        # ----------
        this.X = X
        this.Y = Y

        this.dX = (vector[0])/gameFPS
        this.dY = (vector[1])/gameFPS

        # Logic
        # ----------
        this.size = 0

        this.dmg = 1

        this.health = 0
        
        this.collided = False
        this.collidedList = list()
        this.deathWait = 5

        this.isHostile = True
        
        this.isKang = isKang

        this.delete = False

        this.knockbackWait = 7
        this.knockback = 0

        # Checks for luigi or not, for determining some stats
        if isKang:
            this.health = 1
            this.size = dankeyKang.kangDim
            
        else:
            this.health = 3
            this.size = dankeyKang.notKangDim

        this.width = this.size[0]
        this.height = this.size[1]

    # tick()
    # If collided, fall back, if needs to be deleted, delete, otherwise, move forward
    # ----------
    def tick(this):

        if this.X < -this.size[0] or this.Y < -this.size[1] or this.deathWait == 0:
            this.delete = True

        elif this.health == 0:
            this.dmg = 0
            this.deathWait -= 1

        elif this.collided:
            if this.knockback == 0:
                this.collided = False

            if this.collided:
                this.knockback -=1

        elif not this.collided:
            this.X+=this.dX
            this.Y+=this.dY

    # draw()
    # Simply draw based on what kong this is, draw explosion if dead
    # ----------
    def draw(this, surface):
        if this.isKang:
            surface.blit(dankeyKang.dankeyKangPic, (this.X, this.Y))
            if this.health == 0:
                surface.blit(entity.plosion, (this.X - dankeyKang.kangDim[0]/2, this.Y - dankeyKang.kangDim[1]/2))

        if not this.isKang:
            surface.blit(dankeyKang.notDankeyKangPic, (this.X, this.Y))
            if this.health == 0:
                surface.blit(entity.plosion, (this.X - dankeyKang.notKangDim[0]/3, this.Y - dankeyKang.notKangDim[1]/3))

    # collide()
    # If we haven't collided with this object before, get hurt, and set up the
    # proper collision logic variables
    # ----------
    def collide(this, item):
        for item2 in this.collidedList:
            if item is item2:
                return None
        if not item.isHostile:
            this.collidedList.append(item)
            this.health -= item.dmg

        this.collided = True
        this.knockback = this.knockbackWait

# miku()
# Enemy added for fun, shoots its own shots
# ----------
class miku(entity):
    # Images and variables held by all mikus
    # ----------
    miku1 = 0
    miku2 = 0
    fireChance = 1
    fireTime = 5
    mikuMouthLoc = (67, 89)
    fireVector = (-300, 0)
    mikuSize = (160, 160)
    
    def __init__(this, X, Y, vector, game):

        # Position
        # ----------
        this.X = X
        this.Y = Y

        this.dX = (vector[0])/game.FPS
        this.dY = (vector[1])/game.FPS

        # Logic
        # ----------
        this.size = miku.mikuSize

        this.health = 2
        
        this.collided = False
        this.collidedList = list()
        this.deathWait = 5
        this.mikuFire = 0

        this.isHostile = True

        this.waifu = True
        this.knockbackWait = 7
        this.knockback = 0

        this.delete = False

        this.dmg = 1

        this.width = this.size[0]
        this.height = this.size[1]

        this.game = game

    # tick()
    # If miku needs to be deleted, delete, if she's firing, fire, if she's collided, stay still, else
    # move forward
    # ----------
    def tick(this):

        if this.X < -this.size[0] or this.Y < -this.size[1] or this.deathWait == 0:
            this.delete = True
        
        elif this.health == 0:
            this.dmg = 0
            this.deathWait -= 1
        
        elif this.collided:
            if this.knockback == 0:
                this.collided = False

            if this.collided:
                this.knockback -=1
                
        elif 100*random() < miku.fireChance:
            this.mikuFire = miku.fireTime
        
        elif this.mikuFire > 0:
            if this.mikuFire == this.fireTime:
                this.game.gameEntities[1].append(bulletEntity(this.X + miku.mikuMouthLoc[0], this.Y + miku.mikuMouthLoc[1],
                                                              miku.fireVector, True, 1, this.game.FPS))
            this.mikuFire -= 1

        elif not this.collided:
            this.X+=this.dX
            this.Y+=this.dY

    # draw()
    # If dead, draw explosion, if shooting, draw miku2, else, draw miku1
    # ----------
    def draw(this, surface):
        if this.mikuFire > 0:
            surface.blit(miku.miku2, (this.X, this.Y))

        else:
            surface.blit(miku.miku1, (this.X, this.Y))

        if this.health == 0:
                surface.blit(entity.plosion, (this.X, this.Y))

    # collide()
    # If we haven't collided with this object before, get hurt, and set up the
    # proper collision logic variables
    # ----------
    def collide(this, item):
        for item2 in this.collidedList:
            if item is item2:
                return None
        if not item.isHostile:
            this.collidedList.append(item)
            this.health -= item.dmg

        this.collided = True
        this.knockback = this.knockbackWait

# spawner
# Class that spawns up enemies
# ----------
class spawner:
    def __init__(this, freqN, levelLen, game):
        # Logic
        # ----------
        this.state = levelLen
        this.stage = 0
        this.switch = True
        this.freqN = freqN
        this.game = game

        # Spawn list, done super simply to avoid making a more complicated spawner, can be down better
        this.canSpawn = [miku.mikuSize, dankeyKang.kangDim, dankeyKang.kangDim, dankeyKang.kangDim, dankeyKang.kangDim, dankeyKang.kangDim, dankeyKang.kangDim,
                         dankeyKang.notKangDim, dankeyKang.notKangDim, dankeyKang.notKangDim, miku.mikuSize]
        this.toSpawn = 0
        this.levelLen = levelLen
        this.stdEnemyVector = (-5, 0)

    # generate()
    # Goes up in levels if there are no enemies, making it so more enemies come up, and call the function that gives us where enemies show up
    # If its an enemie's time to spawn, spawn the appropriate one with the standard vector
    # ----------
    def generate(this):
        if this.state >= this.levelLen and this.switch:
            this.toSpawn = list()
            this.state = 0
            this.stage+= 1
            toFire = this.stage*this.freqN
            this.toSpawn = this.generateRects(toFire)

        for item in this.toSpawn:
            if item[0].x == this.state:
                this.switch = False
                if item[1] == dankeyKang.kangDim:
                    this.game.gameEntities[2].append(dankeyKang(this.game.resX, item[0].y, this.stdEnemyVector, True, this.game.FPS))        
                elif item[1] == dankeyKang.notKangDim:
                    this.game.gameEntities[2].append(dankeyKang(this.game.resX, item[0].y, this.stdEnemyVector, False, this.game.FPS))
                elif item[1] == miku.mikuSize:
                    this.game.gameEntities[2].append(miku(this.game.resX, item[0].y, this.stdEnemyVector, this.game))
        
        if not this.switch and len(this.game.gameEntities[2]) == 0:
            this.switch = True

        this.state += 1

    # generateRects()
    # Creates a list of things to spawn, using the level length as the maximum place where an enemy can spawn
    # spawn as many as toFire specifies
    # ----------
    def generateRects(this, toFire):

        spawnList = list()
        
        while toFire > 0:
            for n in range (0, 16):
                
                goSpawn = this.canSpawn[int(len(this.canSpawn)*random())]
                randX = int(this.levelLen*random())
                randY = this.game.topRectSize[1] + int((this.game.resY - 2*this.game.topRectSize[1] - goSpawn[1])*random())

                check = True
                rect0 = Rect(randX, randY, goSpawn[0], goSpawn[1])
                
                if len(spawnList) is not 0:
                    for item in spawnList:
                        if rect0.colliderect(item[0]):
                            check = False

                if check:
                    spawnList.append((rect0, goSpawn))
                    break
                        
            toFire-=1

        return spawnList

# menu
# Logic and graphics for the menu
# ----------
class menu(entity):

    # Graphics
    # ----------
    bg = 0
    select = 0
    selectHilite = 0

    def __init__(this, game):
        # Logic
        # ----------
        this.X = 0
        this.Y = 0
        this.delete = False
        this.collided = False
        this.hilite = False
        this.selectRect = (200, 440, 200+600, 440+120)
        this.game = game

    # tick()
    # Sets the cursor to the right state, diamond if cursor is not over the highlight region, broken x otheriwse
    # ----------
    def tick(this):
        if  this.game.mX > this.selectRect[0] and  this.game.mX <  this.selectRect[2] and this.game.mY >  this.selectRect[1] and  this.game.mY < this.selectRect[3]:
            this.hilite = True
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        else:
            this.hilite = False
            pygame.mouse.set_cursor(*pygame.cursors.diamond)

        return False

    # draw()
    # blits the menu, then the select based on whether or not the mouse is over it
    # ----------
    def draw(this, surface):
        surface.blit(menu.bg, (0, 0))

        if this.hilite:
            surface.blit(menu.selectHilite, (this.selectRect[0], this.selectRect[1]))
        else:
            surface.blit(menu.select, (this.selectRect[0], this.selectRect[1]))

    def collide(this, item):
        None
        
grumpsGame().startGame()
