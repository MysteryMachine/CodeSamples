#Hamlet II
#By Salomao Becker
#This is a 1064 line project created by me in the span of two weeks for a capstone project at ECC. This project was my introductory lesson in Python, so some areas may exhibit some greener coding habits.
#The project was created in a rush of inspiration, where I scrapped my previous work modding Minecraft in Java in favor of learning a new language and more fundamental graphics. 
#Link to a video of the project in action (sound was not implemented due to artistic constraints, as all assets were self created):  http://www.youtube.com/watch?v=3wXEFo4aXCI

import pygame, sys, random, math
from pygame.locals import *
#----------------------------------------------------------------------------------------------
#Setting up scren size variables
FPS = 30
WINDOWWIDTH = 1080
WINDOWHEIGHT = 800
#----------------------------------------------------------------------------------------------
#Color definitions and graphics loading
#             R    G    B
GREEN    = (  40, 255,  40)
NAVYBLUE = (  60,  60, 100)
HPRED    = ( 200,   0,   0)
WHITE    = ( 255, 255, 255)
BLACK    = (   0,   0,   0)
DARKBROWN= (  92,  64,  51)
DARKERBROWN =(61,  42,  37)
ATYELLOW = ( 252, 193,  25)
DARKGRAY = (  30,  30,  30)
MANA_BLUE= (  61,  89, 171)
OFFWHITE = ( 231, 231, 231)
BGCOLOR1 = BLACK
BGCOLOR2 = NAVYBLUE

pygame.init()
FONT = pygame.font.Font(pygame.font.match_font('franklingothicmedium'), 25)
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
fpsClock = pygame.time.Clock()    
pygame.display.set_caption('Game')

#----------------------------------------------------------------------------------------------
#Functions

class Battle:
    #Place variables are all tuples where the zeroeth element is x and the first element is y
    CHAR_NAME_PLACES = (260, (680, 720, 760, 640))

    battle_menu     = pygame.image.load('hrassets/menu.png')
    AT_Bar          = pygame.image.load('hrassets/AT_Bar.png')
    barpic          = pygame.image.load('hrassets/menubar.png')
    cursor          = pygame.image.load('hrassets/cursor.png')
    actiontext      = pygame.image.load('hrassets/actiontext.png')
    MENU_PLACE      = (207, 610)
    ATSIZE          = (147, 37)
    ACTIONSIZE      = actiontext.get_size()
    BUBBLEX         = 200
    CHARSIZE        = (400, 300) #pixels
    CURSORSPACE     = 30
    HELPCENTERPIC   = 20
    
    CHAR_MATRIX = ((20, 180), (220, 300), (60, 400),
                   (WINDOWWIDTH - 120 - CHARSIZE[1], 180),
                   (WINDOWWIDTH - 300 - CHARSIZE[1], 300),
                   (WINDOWWIDTH - 160 - CHARSIZE[1], 400))
    
    menuMatrix = (((CHAR_NAME_PLACES[0] + 390, CHAR_NAME_PLACES[1][0]),    (CHAR_NAME_PLACES[0] + 510, CHAR_NAME_PLACES[1][0])),
                  ((CHAR_NAME_PLACES[0] + 390, CHAR_NAME_PLACES[1][1]),    (CHAR_NAME_PLACES[0] + 510, CHAR_NAME_PLACES[1][1])))

    #Event Stages (for checking key inputs) and Flags
    BATTLE              = 1
    BATTLEMENU          = 2
    SPELLPICK           = 3
    ITEMPICK            = 4
    BATTLETARGETTING    = 5
    SPELLTARGETTING     = 6
    ALLYSPELLTARGETTING = 7
    ITEMTARGETTING      = 8
    RUNSTAGE            = 9
    RESOLVEFIGHT        = 10
    RESOLVESPELL        = 11
    RESOLVEALLYSPELL    = 12
    RESOLVEITEM         = 13
    ENDTURN             = 0

    #Some useful constants
    MENUSPACES          = 3
    NUMBERTEAMS         = 2
    ENEMYPLACE          = 1
    PARTYPLACE          = 0
    AI_WAIT             = 5 #frames
    ENEMY_MOVELIST_SIZE = 4
    BUBBLE_MAX_TRAVEL   = 15

    #Item storing vars
    num_Potion = 5
    num_Elixer = 1
    num_Herb   = 3
    num_Seal   = 3

    #Status effects
    SILENCE, IMG_SILENCE, IMG_SILENCE_E = 'Silence', pygame.image.load('hrassets/status_silence.png'), pygame.image.load('hrassets/status_silence_e.png')
    SLOW, IMG_SLOW, IMG_SLOW_E = 'Slow', pygame.image.load('hrassets/status_slow.png'), pygame.image.load('hrassets/status_slow_e.png')
    RAGE, IMG_RAGE, IMG_RAGE_E = 'Rage', pygame.image.load('hrassets/status_rage.png'), pygame.image.load('hrassets/status_rage_e.png')
    DEAD, IMG_DEAD = 'Dead', pygame.image.load('hrassets/status_death.png')

    def __init__(self, background, party, enemies):
        #Sets up the board
        self.BG                = background
        self.battle            = [party, enemies]
        self.randomizeAT()
        count = 0
        for n in range (0, Battle.NUMBERTEAMS, 1):
            for m in range (0, Battle.MENUSPACES, 1):
                self.battle[n][m].position = count
                count += 1
          
        #Fight starts off in battle stage             
        self.battlestage        = Battle.BATTLE
        self.actor              = None
        self.target             = None
        self.delay              = False
        self.delayAI            = 0
        #Variables for cycling through the menus
        self.menu_cycle         = [1, None, None, None]
        self.menu_spot          = 0
        self.charPlace          = 0
        self.foePlace           = 0
        self.a_targetPlace      = 0
        self.pickMenu           = [0, 0]
        self.spell_Menu         = 0
        self.item_Menu          = [0, 0]
        self.RESOLVEFIGHT_F     = False
        self.RESOLVESPELL_F     = False
        self.RESOLVEALLYSPELL_F = False
        self.RESOLVEITEM_F      = False
        self.AT_Var             = 0
        self.bubblepos          = -15
        self.bubbleswitch       = True
    
    def startBattle (self):
        while True:

            #Winning the battle causes this fucntion to end
            if self.battle[Battle.ENEMYPLACE][0].status == Battle.DEAD and self.battle[Battle.ENEMYPLACE][1].status == Battle.DEAD and self.battle[Battle.ENEMYPLACE][2].status == Battle.DEAD:
                return

            self.tickAI()
            DISPLAYSURF.blit(self.BG, (0,0))
            self.menu_cycle[self.menu_spot] = self.battlestage
            self.getTargets()         
            self.eventCheck()    
            
            #Animates characters & updates AT bars
            for n in range (0, Battle.NUMBERTEAMS, 1):
                for m in range (0, Battle.MENUSPACES, 1):
                    self.battle[n][m].animate(self)

            #Draws GUI and cursor    
            self.drawBattleGUI()
            self.drawCursor()

            #Causes damage and stuff to happen after you execute an action (the resolving loop)
            if self.target != None and self.actor != None and self.delay:
                self.resolving(self.actor, self.target)
                self.endofMove_Reset()
                for n in range (0, Battle.NUMBERTEAMS, 1):
                    for m in range (0, Battle.MENUSPACES, 1):
                        self.battle[n][m].endOfTurn()    
                if self.battle[Battle.ENEMYPLACE][0].status != Battle.DEAD or self.battle[Battle.ENEMYPLACE][0].health != 0:
                    self.foePlace = 0
                elif self.battle[Battle.ENEMYPLACE][1].status != Battle.DEAD or self.battle[Battle.ENEMYPLACE][1].health != 0:
                    self.foePlace = 1
                else:
                    self.foePlace = 2
                self.resetMenu()

            if not self.delay:
                for n in range (0, Battle.NUMBERTEAMS, 1):
                    for m in range (0, Battle.MENUSPACES, 1):
                        self.battle[n][m].endOfTurn()
                        
            #Causes above loop to not occur if the resolving loop executes
            if self.delay:
                self.delay = False

            #Helps AT Bars to blink
            if self.AT_Var == Unit.CHARBLINK_RESET:
                self.AT_Var = 0
            else:
                self.AT_Var += 1

            self.makeStatusBubbleBounce()
              
            pygame.display.update()
            fpsClock.tick(FPS)

    #Battle Functions
    def resolving(self, actor, target):
        #Checking flags for all resolves, it's why they're useful (other than animation)
        if self.RESOLVEFIGHT_F:
               fight.moveEffect(self.actor, self.target)
        if self.RESOLVEITEM_F:
            if self.item_Menu[0] == 0 and self.item_Menu[1] == 0:
                potionMove.moveEffect(self.actor, self.target)
            elif self.item_Menu[0] == 0 and self.item_Menu[1] == 1:
                herbMove.moveEffect(self.actor, self.target)
            elif self.item_Menu[0] == 1 and self.item_Menu[1] == 0:
                elixerMove.moveEffect(self.actor, self.target)
            elif self.item_Menu[0] == 1 and self.item_Menu[1] == 1:
                sealMove.moveEffect(self.actor, self.target)
        if self.RESOLVESPELL_F:
            self.actor.moveList[self.spell_Menu].moveEffect(self.actor, self.target)
        if self.RESOLVEALLYSPELL_F:
            self.actor.moveList[self.spell_Menu].moveEffect(self.actor, self.target)

    def enemyAI(self):
        #Picks a random valid party memeber and hits him with a random move
        randenemy = random.randrange(0, Battle.MENUSPACES, 1)
        
        while True:
            randally = random.randrange(0, Battle.MENUSPACES, 1)
            if self.battle[Battle.PARTYPLACE][randally] != None:
                if self.battle[Battle.PARTYPLACE][randally].status != Battle.DEAD:
                    break
        if self.battle[Battle.ENEMYPLACE][randenemy] != None:
            if self.battle[Battle.ENEMYPLACE][randenemy].canMove:
                self.battle[Battle.ENEMYPLACE][randenemy].moveList[random.randrange(0, Battle.ENEMY_MOVELIST_SIZE, 1)].moveEffect(self.battle[1][randenemy], self.battle[0][randally])
                self.battle[Battle.ENEMYPLACE][randenemy].resetAT()
                return random.randrange(Unit.BLINKVAR + Battle.AI_WAIT, FPS + Battle.AI_WAIT, 1)
        return 0

    def tickAI(self):
        if self.delayAI == 0:
            self.delayAI = self.enemyAI()
        else:
            self.delayAI -= 1

    def getTargets(self):
        if self.battlestage == Battle.BATTLEMENU:
            self.actor = self.battle[Battle.PARTYPLACE][self.charPlace]
        elif self.battlestage == Battle.RESOLVEFIGHT:
            self.target =  self.battle[Battle.ENEMYPLACE][self.foePlace]
            self.delay = True
        elif self.battlestage == Battle.RESOLVEITEM or self.battlestage == Battle.RESOLVEALLYSPELL:
            self.target = self.battle[Battle.PARTYPLACE][self.a_targetPlace]
            self.delay = True
        elif self.battlestage == Battle.RESOLVESPELL:
            self.target = self.battle[Battle.ENEMYPLACE][self.foePlace]
            self.delay = True

    def endofMove_Reset(self):
        self.actor.resetAT()
        self.target = None
        self.actor = None
        self.RESOLVEFIGHT_F = False
        self.RESOLVESPELL_F = False
        self.RESOLVEALLYSPELL_F = False
        self.RESOLVEITEM_F = False
        self.battlestage = Battle.BATTLE
        self.a_targetPlace = 0

    #Battle Menu related functions
    def eventCheck(self):
        '''This  function handles all of my battle user input, many if statements to handle the 10ish menus you can get during battle'''        
        if self.battlestage == Battle.BATTLE:
            for event in pygame.event.get():
                if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                if (event.type == KEYUP and event.key == K_UP and self.charPlace > 0):
                            self.charPlace -= 1
                if (event.type == KEYUP and event.key == K_DOWN and self.charPlace < 2):
                            self.charPlace += 1
                if (self.canReturn(event)):
                    if self.battle[Battle.PARTYPLACE][self.charPlace].canMove:
                        self.battlestage = Battle.BATTLEMENU
                        self.menu_spot += 1
        if self.battlestage > Battle.BATTLE and self.battle[Battle.PARTYPLACE][self.charPlace].status == Battle.DEAD:
            self.resetMenu()
            self.battlestage = Battle.BATTLE
                  
        elif self.battlestage == Battle.BATTLEMENU:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if (self.canUpArrow(event, self.pickMenu, 2)):
                            self.pickMenu[1] -= 1
                if (self.canDownArrow(event, self.pickMenu, 2)):
                            self.pickMenu[1] += 1
                if (self.canLeftArrow(event, self.pickMenu, 2)):
                            self.pickMenu[0] -= 1
                if (self.canRightArrow(event, self.pickMenu, 2)):
                            self.pickMenu[0] += 1
                if (self.canReturn(event)):
                    if self.pickMenu[0] == 0 and self.pickMenu[1] == 0:
                        self.battlestage = Battle.BATTLETARGETTING
                        self.menu_spot += 1
                    elif self.pickMenu[0] == 1 and self.pickMenu[1] == 0:
                        self.menu_spot += 1
                        self.battlestage = Battle.SPELLPICK
                    elif self.pickMenu[0] == 0 and self.pickMenu[1] == 1:
                        self.menu_spot += 1
                        self.battlestage = Battle.ITEMPICK
                    elif self.pickMenu[0] == 1 and self.pickMenu[1] == 1:
                        self.menu_spot += 1
                        self.battlestage = Battle.RUNSTAGE
                if event.type == KEYUP and event.key == K_ESCAPE:
                    self.returntoPrevMenu()
                    self.pickMenu = [0, 0]

        elif self.battlestage == Battle.ITEMPICK:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if (self.canUpArrow(event, self.item_Menu, 2)):
                        self.item_Menu[1] -= 1
                if (self.canDownArrow(event, self.item_Menu, 2)):
                        self.item_Menu[1] += 1
                if (self.canLeftArrow(event, self.item_Menu, 2)):
                        self.item_Menu[0] -= 1
                if (self.canRightArrow(event, self.item_Menu, 2)):
                        self.item_Menu[0] += 1
                if (self.canReturn(event)):
                    if (self.item_Menu[0] == 0 and self.item_Menu[1] == 0 and Battle.num_Potion > 0):
                        self.battlestage = Battle.ITEMTARGETTING 
                        self.menu_spot += 1
                    elif(self.item_Menu[0] == 1 and self.item_Menu[1] == 0 and Battle.num_Elixer > 0):
                        self.battlestage = Battle.ITEMTARGETTING 
                        self.menu_spot += 1
                    elif(self.item_Menu[0] == 0 and self.item_Menu[1] == 1 and Battle.num_Herb > 0):
                        self.battlestage = Battle.ITEMTARGETTING 
                        self.menu_spot += 1
                    elif(self.item_Menu[1] == 1 and self.item_Menu[1] == 1 and Battle.num_Seal > 0):
                        self.battlestage = Battle.ITEMTARGETTING 
                        self.menu_spot += 1
                if event.type == KEYUP and event.key == K_ESCAPE:
                    self.returntoPrevMenu()
                    self.item_Menu[0] = 0
                    self.item_Menu[1] = 0

        elif self.battlestage == Battle.SPELLPICK:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYUP and event.key == K_UP and self.spell_Menu > 0):
                            self.spell_Menu -= 1
                if (event.type == KEYUP and event.key == K_DOWN and self.spell_Menu < 2):
                    if self.battle[Battle.PARTYPLACE][self.charPlace].moveList[self.spell_Menu + 1] != voidMove:
                            self.spell_Menu += 1
                if (self.canReturn(event)  and self.battle[Battle.PARTYPLACE][self.charPlace].status != Battle.SILENCE):
                    if self.magicColorPick(self.battle[Battle.PARTYPLACE][self.charPlace].moveList[self.spell_Menu], self.battle[Battle.PARTYPLACE][self.charPlace]) == WHITE:
                        if self.battle[Battle.PARTYPLACE][self.charPlace].moveList[self.spell_Menu].ISALLY:
                            self.battlestage = Battle.ALLYSPELLTARGETTING
                            self.menu_spot += 1
                        else:
                            self.battlestage = Battle.SPELLTARGETTING
                            self.menu_spot += 1
                if event.type == KEYUP and event.key == K_ESCAPE:
                    self.returntoPrevMenu()
                    self.spell_Menu = 0

        elif self.battlestage == Battle.SPELLTARGETTING:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYUP and event.key == K_UP and self.foePlace > 0):
                    if self.battle[Battle.PARTYPLACE][self.foePlace - 1].status != Battle.DEAD:
                        self.foePlace -= 1
                    elif self.foePlace - 2 > -1:
                        if self.battle[Battle.ENEMYPLACE][self.foePlace - 2].status != Battle.DEAD:
                            self.foePlace -= 2
                if (event.type == KEYUP and event.key == K_DOWN and self.foePlace < 2 and self.battle[Battle.ENEMYPLACE][self.foePlace] != None):
                    if self.battle[Battle.PARTYPLACE][self.foePlace + 1].status != Battle.DEAD:
                        self.foePlace += 1
                    elif self.foePlace + 2 < 4:
                        if self.battle[Battle.ENEMYPLACE][self.foePlace + 2].status != Battle.DEAD:
                            self.foePlace += 2
                if (self.canReturn(event)):
                    self.battlestage = Battle.RESOLVESPELL
                    self.RESOLVESPELL_F = True
                if event.type == KEYUP and event.key == K_ESCAPE:
                    self.returntoPrevMenu()
                    if self.battle[Battle.ENEMYPLACE][0].status != Battle.DEAD:
                        self.foePlace = 0
                    elif battle[Battle.ENEMYPLACE][1].status != Battle.DEAD:
                        self.foePlace = 1
                    else:
                        self.foePlace = 2
               
        elif self.battlestage == Battle.BATTLETARGETTING:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYUP and event.key == K_UP and self.foePlace > 0):
                    if self.battle[Battle.ENEMYPLACE][self.foePlace - 1].status != Battle.DEAD:
                        self.foePlace -= 1
                    elif self.foePlace - 2 > -1:
                        if self.battle[Battle.ENEMYPLACE][self.foePlace - 2].status != Battle.DEAD:
                            self.foePlace -= 2
                if (event.type == KEYUP and event.key == K_DOWN and self.foePlace < 2 and self.battle[Battle.ENEMYPLACE][self.foePlace] != None):
                    if self.battle[Battle.ENEMYPLACE][self.foePlace + 1].status != Battle.DEAD:
                        self.foePlace += 1
                    elif self.foePlace + 2 < 4:
                        if self.battle[Battle.ENEMYPLACE][self.foePlace + 2].status != Battle.DEAD:
                            self.foePlace += 2
                if (self.canReturn(event)):
                    self.battlestage = Battle.RESOLVEFIGHT
                    self.RESOLVEFIGHT_F = True
                if event.type == KEYUP and event.key == K_ESCAPE:
                    self.returntoPrevMenu()
                    if self.battle[Battle.ENEMYPLACE][0].status != Battle.DEAD:
                        self.foePlace = 0
                    elif battle[Battle.ENEMYPLACE][1].status != Battle.DEAD:
                        self.foePlace = 1
                    else:
                        self.foePlace = 2

        elif self.battlestage == Battle.ITEMTARGETTING:
            for event in pygame.event.get():
                if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                if (event.type == KEYUP and event.key == K_UP and self.a_targetPlace  > 0):
                            self.a_targetPlace  -= 1
                if (event.type == KEYUP and event.key == K_DOWN and self.a_targetPlace  < 2):
                            self.a_targetPlace  += 1
                if (self.canReturn(event)):
                    self.battlestage = Battle.RESOLVEITEM
                    self.RESOLVEITEM_F = True
                if event.type == KEYUP and event.key == K_ESCAPE:
                    self.returntoPrevMenu()
                    self.a_targetPlace = 0

        elif self.battlestage == Battle.ALLYSPELLTARGETTING:
            for event in pygame.event.get():
                if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                if (event.type == KEYUP and event.key == K_UP and self.a_targetPlace  > 0):
                            self.a_targetPlace  -= 1
                if (event.type == KEYUP and event.key == K_DOWN and self.a_targetPlace  < 2):
                            self.a_targetPlace  += 1
                if (self.canReturn(event)):
                    self.battlestage = Battle.RESOLVEALLYSPELL
                    self.RESOLVEALLYSPELL_F = True
                if event.type == KEYUP and event.key == K_ESCAPE:
                    self.returntoPrevMenu()
                    self.a_targetPlace = 0
            
    def resetMenu(self):
        self.menu_cycle = [1, None,None, None]
        self.menu_spot = 0

    def returntoPrevMenu(self):
        self.menu_cycle[self.menu_spot] = None
        self.menu_spot -= 1
        self.battlestage = self.menu_cycle[self.menu_spot]

    #Functions that are here to make code a little more read-able. Only works on 2D menus.
    def canUpArrow (self, event, menu, ysize):
        return (event.type == KEYUP and event.key == K_UP and menu[1] > 0)

    def canDownArrow (self, event, menu, ysize):
        return (event.type == KEYUP and event.key == K_DOWN and menu[1] < ysize - 1)

    def canLeftArrow (self, event, menu, xsize):
        return (event.type == KEYUP and event.key == K_LEFT and menu[0] > 0)

    def canRightArrow (self, event, menu, xsize):
        return (event.type == KEYUP and event.key == K_RIGHT and menu[0] < xsize - 1)

    def canReturn (self, event):
        return (event.type == KEYUP and event.key == K_RETURN)

    def drawCursor (self):
        '''This function draws the highlights around the picture you are selecting, uses some flags in the
        process so that any previous highlight you used in a previous menu stays highlighted, so you can see what you're doing.'''
        
        if self.battlestage != Battle.ITEMTARGETTING and self.battlestage != Battle.ALLYSPELLTARGETTING and self.battlestage != Battle.ITEMPICK and self.battlestage != Battle.SPELLPICK:
            DISPLAYSURF.blit(Battle.cursor, (Battle.CHAR_NAME_PLACES[0] - Battle.CURSORSPACE, Battle.CHAR_NAME_PLACES[1][self.charPlace]))
        
        if self.battlestage == Battle.BATTLEMENU:
            DISPLAYSURF.blit(Battle.cursor, (Battle.menuMatrix[self.pickMenu[1]][self.pickMenu[0]][0] - Battle.CURSORSPACE, Battle.menuMatrix[self.pickMenu[1]][self.pickMenu[0]][1]))
                    
        if self.battlestage == Battle.BATTLETARGETTING or self.battlestage == Battle.SPELLTARGETTING:
            DISPLAYSURF.blit(Battle.cursor, (Battle.menuMatrix[0][0][0] - Battle.CURSORSPACE, Battle.CHAR_NAME_PLACES[1][self.foePlace] - Battle.HELPCENTERPIC))
          
        if self.battlestage == Battle.ITEMPICK or self.battlestage == Battle.ITEMTARGETTING:
            DISPLAYSURF.blit(Battle.cursor, (Battle.menuMatrix[self.item_Menu[1]][self.item_Menu[0]][0] - Battle.CURSORSPACE, Battle.menuMatrix[self.item_Menu[1]][self.item_Menu[0]][1]))

        if self.battlestage == Battle.ITEMTARGETTING or self.battlestage == Battle.ALLYSPELLTARGETTING:
            DISPLAYSURF.blit(Battle.cursor, (Battle.CHAR_NAME_PLACES[0] - Battle.CURSORSPACE, Battle.CHAR_NAME_PLACES[1][self.a_targetPlace]))

        if self.battlestage == Battle.SPELLPICK or self.battlestage == Battle.ALLYSPELLTARGETTING:
            DISPLAYSURF.blit(Battle.cursor, (Battle.menuMatrix[0][0][0] - Battle.CURSORSPACE, Battle.CHAR_NAME_PLACES[1][self.spell_Menu] - Battle.HELPCENTERPIC))
        
        else:
            return None
        
    def drawPartyInfo(self):
        for n in range (0, Battle.MENUSPACES, 1):
            if self.battle[0][n] != None:
                DISPLAYSURF.blit(FONT.render(self.battle[Battle.PARTYPLACE][n].NAME, True, WHITE), (Battle.CHAR_NAME_PLACES[0], Battle.CHAR_NAME_PLACES[1][n]))
                DISPLAYSURF.blit(FONT.render(str(math.floor(self.battle[Battle.PARTYPLACE][n].health)), True, WHITE), (Battle.CHAR_NAME_PLACES[0] + 100, Battle.CHAR_NAME_PLACES[1][n]))
                DISPLAYSURF.blit((FONT.render(str(math.floor(self.battle[Battle.PARTYPLACE][n].magic)), True, WHITE)), (Battle.CHAR_NAME_PLACES[0] + 150, Battle.CHAR_NAME_PLACES[1][n]))
                DISPLAYSURF.blit(Battle.AT_Bar, (Battle.CHAR_NAME_PLACES[0] + 200, Battle.CHAR_NAME_PLACES[1][n] - 5))
                self.battle[0][n].drawAT(self)
        DISPLAYSURF.blit((FONT.render('Name', True, WHITE)), (Battle.CHAR_NAME_PLACES[0], Battle.CHAR_NAME_PLACES[1][3]))
        DISPLAYSURF.blit((FONT.render('HP', True, WHITE)), (Battle.CHAR_NAME_PLACES[0] + 100, Battle.CHAR_NAME_PLACES[1][3]))
        DISPLAYSURF.blit((FONT.render('MP', True, WHITE)), (Battle.CHAR_NAME_PLACES[0] + 150, Battle.CHAR_NAME_PLACES[1][3]))
        DISPLAYSURF.blit(Battle.barpic, (Battle.CHAR_NAME_PLACES[0] + 280, Battle.CHAR_NAME_PLACES[1][0] - 84))

    def drawMenu (self):
        DISPLAYSURF.blit(FONT.render('Fight', True, WHITE), Battle.menuMatrix[0][0])
        DISPLAYSURF.blit(FONT.render('Magic', True, WHITE), Battle.menuMatrix[0][1])
        DISPLAYSURF.blit(FONT.render('Item', True, WHITE), Battle.menuMatrix[1][0])
        DISPLAYSURF.blit(FONT.render('Run' , True, WHITE), Battle.menuMatrix[1][1])

    def drawItemMenu(self):
        DISPLAYSURF.blit(FONT.render('Potion', True, self.itemsColorPick(Battle.num_Potion)), Battle.menuMatrix[0][0])
        DISPLAYSURF.blit(FONT.render('Elixer', True, self.itemsColorPick(Battle.num_Elixer)), Battle.menuMatrix[0][1])
        DISPLAYSURF.blit(FONT.render('Herb'  , True, self.itemsColorPick(Battle.num_Herb))  , Battle.menuMatrix[1][0])
        DISPLAYSURF.blit(FONT.render('Seal'  , True, self.itemsColorPick(Battle.num_Seal))  , Battle.menuMatrix[1][1])

    def itemsColorPick(self, item):
        if item >= 1:
            return WHITE
        return DARKGRAY

    def drawBattleMenu(self):
        for n in range (0, Battle.MENUSPACES, 1):
            if self.battle[0][n] != None and self.battle[Battle.ENEMYPLACE][n].status != Battle.DEAD:
                DISPLAYSURF.blit(FONT.render(self.battle[Battle.ENEMYPLACE][n].NAME, True, WHITE), (Battle.menuMatrix[0][0][0], Battle.CHAR_NAME_PLACES[1][n] - 20))

    def drawMagicMenu(self):
        for n in range (0, Battle.MENUSPACES, 1):
            if self.battle[Battle.PARTYPLACE][self.charPlace] != None and self.battle[Battle.PARTYPLACE][self.charPlace].moveList[n] != voidMove:
                DISPLAYSURF.blit(FONT.render(self.battle[Battle.PARTYPLACE][self.charPlace].moveList[n].NAME, True, self.magicColorPick(self.battle[0][self.charPlace].moveList[n], self.battle[Battle.PARTYPLACE][self.charPlace])), (Battle.menuMatrix[0][0][0], Battle.CHAR_NAME_PLACES[1][n] - 20))

    def magicColorPick(self, spell, caster):
        if caster.magic < spell.MP or caster.status == Battle.SILENCE:
            return DARKGRAY
        return WHITE

    def drawBattleGUI (self):
        DISPLAYSURF.blit(self.battle_menu, Battle.MENU_PLACE)
        self.drawPartyInfo()
        if self.battlestage == Battle.BATTLE:
            self.drawBattleMenu()
        if self.battlestage == Battle.BATTLEMENU :
            self.drawMenu()
        if self.battlestage == Battle.ITEMPICK or self.menu_cycle[3] == Battle.ITEMTARGETTING:
            self.drawItemMenu()
        if self.battlestage == Battle.BATTLETARGETTING or self.battlestage == Battle.SPELLTARGETTING:
            self.drawBattleMenu()
        if self.battlestage == Battle.SPELLPICK or self.battlestage == Battle.ALLYSPELLTARGETTING:
            self.drawMagicMenu ()

    def randomizeAT(self):
        for n in range (0, Battle.NUMBERTEAMS, 1):
            for m in range (0, Battle.MENUSPACES, 1):
                if self.battle[n][m] != None:
                    self.battle[n][m].currentAT = random.randint(0, 100)

    def makeStatusBubbleBounce(self):
        if self.bubblepos == 15:
            self.bubbleswitch = False
        elif self.bubblepos ==  -15:
            self.bubbleswitch = True
            
        if self.bubbleswitch:
            self.bubblepos += 1
        else:
            self.bubblepos -= 1
#----------------------------------------------------------------------------------------------
class Move: #extend and override methods
    def __init__ (self, name, power, accuraccy, secondaryaccuracy = 0, magicCost = 0, isAlly = False,  isMagic = True, damage = True):
        self.NAME        = name
        self.POWER       = power
        self.ACCURACY    = accuraccy
        self.ACCURACY2   = secondaryaccuracy#<-------------------Accuracy for the effects of skills
        self.MP          = magicCost
        self.ISALLY      = isAlly#<------------------------------Flag for healing moves
        self.ISMAGIC     = isMagic#<-----------------------------Flag for skills that require the magic animation
        self.DAMAGE      = damage

    def moveEffect(self, user, target):
        #Triggers animation variables
        if self.innerCanMoveEffect(user, target):
            user.magic -= self.MP
            if self.ISMAGIC:
                user.isAnimating_C = True
            else:
                user.isAnimating_F = True
            if (random.random() < self.ACCURACY) and self.DAMAGE: #Rolls for misses
                dmg = math.floor((user.POWER - (target.DEFENSE/2))*((4.5 + random.random())/5)*self.POWER)
                if dmg <= 0 and not self.ISALLY: #Damage cannot be less than 1
                    dmg = 1
                #Triggers blinking in target
                if target.health - dmg < target.HEALTH:
                    if not self.ISMAGIC:
                        target.blinkingVar = user.attack1_time + user.attackwait + Unit.BLINKVAR
                        if target.lastDamageTook[0] == '0':
                            target.lastDamageTook[0] = str(abs(dmg))
                            target.damageCount[0] = Unit.DAMAGECOUNTER
                        else:
                            target.damageCount[1] = Unit.DAMAGECOUNTER
                            target.lastDamageTook[1] = str(abs(dmg))
                    else:
                        target.blinkingVar = user.cast1_time + Unit.BLINKVAR
                        if target.lastDamageTook[0] == '0':
                            target.lastDamageTook[0] = str(abs(dmg)) + ' '
                            target.damageCount[0] = Unit.DAMAGECOUNTER
                        elif self.DAMAGE:
                            target.damageCount[1] = Unit.DAMAGECOUNTER
                            target.lastDamageTook[1] = str(abs(dmg)) + ' '

                if dmg <= 0:
                    if target.lastDamageTook[0] == '0':
                        target.damagecolor[0] = GREEN
                    else:
                        target.damagecolor[1] = GREEN
                else:
                    if target.lastDamageTook[0] == '0':
                        target.damagecolor[0] = WHITE
                    else:
                        target.damagecolor[1] = WHITE
                        
                #Healing cannot heal more than HEALTH (max health)
                if target.health - dmg > target.HEALTH:
                    target.damageCount[1] = Unit.DAMAGECOUNTER
                    target.lastDamageTook[1] = str((int)(target.HEALTH- target.health))
                    target.health = target.HEALTH
                    return True 

                #HP cannot go under 0
                elif dmg <= target.health:
                    target.health -= dmg
                    return True
                #Triggers death
                else:
                    target.health = 0

                    if not self.ISMAGIC:
                        target.deadAnimWait = user.attack1_time + user.attackwait + Unit.BLINKVAR
                    else:
                        target.deadAnimWait = user.cast1_time + Unit.BLINKVAR
                    return True
            elif self.DAMAGE:
                if target.lastDamageTook[0] == '0':
                    target.lastDamageTook[0] = 'Miss'
                    target.damageCount[0] = Unit.DAMAGECOUNTER
                    target.damagecolor[0] = WHITE
                else:
                    target.damageCount[1] = Unit.DAMAGECOUNTER
                    target.lastDamageTook[1] = 'Miss'
                    target.damagecolor[1] = WHITE
        return  False
    
    def innerCanMoveEffect (self, user, target):
        return target.status != Battle.DEAD
    
    def canMoveEffect (self, user, target):
        return target.status != Battle.DEAD
#----------------------------------------------------------------------------------------------            
class Ability:
    def __init__ (self, name, description, effect):
        return
        
    def abilityEffect (self):
        return
    
    def canAbilityEffect (self, phase):
        return false
#----------------------------------------------------------------------------------------------
class Unit: #Extend to easily make new units
    BLINKVAR        = 12
    DEADANIM        = 9
    DEADANIM2       = 6
    DEADANIM3       = 3
    IDLENUM         = 0.35
    IDLEVARIANCE    = 3
    CHARBLINK_VAR   = 28
    CHARBLINK_RESET = 30
    MAX_AT          = 100
    DAMAGECOUNTER   = 30
    
    def __init__ (self, name, move, hlth, mgc, power, defense, speed, a1, a2, a3, a4, a5, a6, img1, img2, img3, img4, img5, img6, img7, img8, img9):
        #Character properties
        self.NAME       = name
        self.HEALTH     = hlth
        self.health     = hlth
        self.MAGIC      = mgc
        self.magic      = mgc
        self.POWER      = power
        self.DEFENSE    = defense
        self.SPEED      = speed
        self.status     = None
        self.moveList   = move
        self.currentAT  = 0

        #Animation variables
        self.idle1          = img1 
        self.idle2          = img2 
        self.attack1        = img3 
        self.attack2        = img4 
        self.cast1          = img5 
        self.cast2          = img6 
        self.dead1          = img7
        self.dead2          = img8
        self.dead3          = img9
        self.animplace      = 0
        self.isAnimating_F  = False
        self.isAnimating_C  = False
        self.canMove        = False
        self.position       = 0
        self.attackwait     = a1
        self.attack1_time   = a2
        self.attack2_time   = a3
        self.cast1_time     = a4
        self.cast2_time     = a5
        self.idlewait       = a6    

        #All counters for animation
        self.idle           = 0
        self.deadAnim       = Unit.DEADANIM
        self.deadAnimWait   = 1
        self.blinkingVar    = 0
        self.damageCount    = [0, 0]
        self.lastDamageTook = ['0', '0']
        self.damagecolor    = [WHITE, WHITE]
    
    def animate (self, battleclass):
        '''Handles most of the character animation process'''
        #For when a character comes back to life
        if self.status != Battle.DEAD and self.deadAnim == 0:
            self.deadAnim = Unit.DEADANIM
            self.deadAnimWait = 1

        #Death animation
        if self.deadAnimWait == 0 and self.status == Battle.DEAD and self.blinkingVar == 0 and not self.isAnimating_F and not self.isAnimating_C:
            if self.deadAnim == 0 and self.position > 2:
                return
            elif self.deadAnim >= Unit.DEADANIM2:
                DISPLAYSURF.blit(self.dead1, Battle.CHAR_MATRIX[self.position])
            elif self.deadAnim  >= Unit.DEADANIM3:
                DISPLAYSURF.blit(self.dead2, Battle.CHAR_MATRIX[self.position])
            else:
                DISPLAYSURF.blit(self.dead3, Battle.CHAR_MATRIX[self.position])

        #Blinkvar makes a character blink if he takes damage, will be 0 (this bottom statement will be true) unless target
        #takes some form of damage.
        elif self.blinkingVar%(Unit.BLINKVAR/3) < 3 or self.blinkingVar > Unit.BLINKVAR:
            #Uses attack animation
            if self.isAnimating_F:
                self.animplace += 1
                if   self.animplace <  self.attackwait:   DISPLAYSURF.blit(self.idle1, Battle.CHAR_MATRIX[self.position])
                elif self.animplace  < self.attack1_time:  DISPLAYSURF.blit(self.attack1, Battle.CHAR_MATRIX[self.position])
                elif self.animplace  < self.attack2_time:  DISPLAYSURF.blit(self.attack2, Battle.CHAR_MATRIX[self.position])
                else:
                    self.animplace, self.isAnimating_F = 0, False
                    DISPLAYSURF.blit(self.idle1, Battle.CHAR_MATRIX[self.position])
            #Uses casting animation
            elif self.isAnimating_C:
                self.animplace += 1
                if   self.animplace <  self.attackwait:   DISPLAYSURF.blit(self.idle1, Battle.CHAR_MATRIX[self.position])
                elif self.animplace  < self.cast1_time:  DISPLAYSURF.blit(self.cast1, Battle.CHAR_MATRIX[self.position])
                elif self.animplace  < self.cast2_time:  DISPLAYSURF.blit(self.cast2, Battle.CHAR_MATRIX[self.position])
                else:
                    self.animplace, self.isAnimating_C = 0, False
                    DISPLAYSURF.blit(self.idle1, Battle.CHAR_MATRIX[self.position])
                    
            #Idle animation, psuedo random waiting time makes characters lifelike
            else:
                if self.idle > self.idlewait:
                    self.idle = 0
                if self.idle < self.idlewait/2:
                    DISPLAYSURF.blit(self.idle1, Battle.CHAR_MATRIX[self.position])
                    if random.random() > Unit.IDLENUM:
                        self.idle += random.randint(0, Unit.IDLEVARIANCE)
                else:
                    DISPLAYSURF.blit(self.idle2, Battle.CHAR_MATRIX[self.position])
                    if random.random() > Unit.IDLENUM:
                        self.idle += random.randint(0, Unit.IDLEVARIANCE)
        if self.blinkingVar != 0:
            self.blinkingVar -= 1
        self.drawStatus(battleclass)
        self.drawTakingDamage()

    def drawStatus(self, battleclass):
        if self.position < 3:
            if self.status == Battle.DEAD:
                DISPLAYSURF.blit(Battle.IMG_DEAD, (Battle.CHAR_MATRIX[self.position][0] + Battle.BUBBLEX, Battle.CHAR_MATRIX[self.position][1] + battleclass.bubblepos))
            elif self.status == Battle.SILENCE :
                DISPLAYSURF.blit(Battle.IMG_SILENCE, (Battle.CHAR_MATRIX[self.position][0] + Battle.BUBBLEX, Battle.CHAR_MATRIX[self.position][1]+ battleclass.bubblepos))
            elif self.status == Battle.RAGE:
                DISPLAYSURF.blit(Battle.IMG_RAGE, (Battle.CHAR_MATRIX[self.position][0] + Battle.BUBBLEX, Battle.CHAR_MATRIX[self.position][1]+ battleclass.bubblepos))
            elif self.status == Battle.SLOW:
                DISPLAYSURF.blit(Battle.IMG_SLOW, (Battle.CHAR_MATRIX[self.position][0]+ Battle.BUBBLEX, Battle.CHAR_MATRIX[self.position][1] + battleclass.bubblepos))
        else:
            if self.status == Battle.SILENCE :
                DISPLAYSURF.blit(Battle.IMG_SILENCE_E, (Battle.CHAR_MATRIX[self.position][0]+ Battle.CHARSIZE[0] - 1.5*Battle.BUBBLEX, Battle.CHAR_MATRIX[self.position][1] + battleclass.bubblepos))
            elif self.status == Battle.RAGE:
                DISPLAYSURF.blit(Battle.IMG_RAGE_E, (Battle.CHAR_MATRIX[self.position][0]+ Battle.CHARSIZE[0]  - 1.5*Battle.BUBBLEX, Battle.CHAR_MATRIX[self.position][1] + battleclass.bubblepos))
            elif self.status == Battle.SLOW:
                DISPLAYSURF.blit(Battle.IMG_SLOW_E, (Battle.CHAR_MATRIX[self.position][0]+ Battle.CHARSIZE[0] - 1.5*Battle.BUBBLEX, Battle.CHAR_MATRIX[self.position][1] + battleclass.bubblepos))
        
    def drawTakingDamage(self):
        centerizer1 = 80
        centerizer2 = 75
        centerizer3 = 100
        for n in range (0, 2, 1):
            if  self.blinkingVar < Unit.BLINKVAR:
                if self.damageCount[n] > 0:
                    if self.position < 3:
                        DISPLAYSURF.blit(FONT.render(self.lastDamageTook[n], True, self.damagecolor[n]), (Battle.CHAR_MATRIX[self.position][0] + centerizer1, Battle.CHAR_MATRIX[self.position][1] - centerizer2 + Battle.CHARSIZE[1]*self.damageCount[n]/centerizer3))
                    if self.position >= 3:
                        DISPLAYSURF.blit(FONT.render(self.lastDamageTook[n], True, self.damagecolor[n]), (Battle.CHAR_MATRIX[self.position][0] + Battle.CHARSIZE[0] - centerizer1, Battle.CHAR_MATRIX[self.position][1] - centerizer2 + Battle.CHARSIZE[1]*self.damageCount[n]/centerizer3))
                self.damageCount[n] -= 1
            elif self.damageCount[n] == 0:
                self.damagecolor[n] = WHITE
            
    def drawAT(self, battleclass):
        if self.atBlinker(battleclass):
            pygame.draw.rect(DISPLAYSURF, OFFWHITE, (Battle.CHAR_NAME_PLACES[0] + 225, Battle.CHAR_NAME_PLACES[1][self.position] + 7, (Battle.ATSIZE[0] - 52)*(self.currentAT)/100, Battle.ATSIZE[1] - 25)) 

    def atBlinker(self, battleclass):
        '''Causes AT bar to blink when full, blinks whenever AT_Var equals CHARBLINK_VAR''' 
        if self.currentAT != Unit.MAX_AT:
            return True
        if battleclass.AT_Var < Unit.CHARBLINK_VAR:
            return True
        return False
       
    def endOfTurn (self):
        '''Handles characters dying and time moving for them, initates the death animation cycle'''
        if self.deadAnimWait != 0 and self.status == Battle.DEAD:
            self.deadAnimWait -= 1
        if self.status == Battle.DEAD and self.deadAnim != 0 and self.deadAnimWait == 0:
            self.deadAnim -= 1
            
        if self.health == 0 and self.status != Battle.DEAD:
            self.status = Battle.DEAD
            self.currentAT = 0
   
        if self.status != Battle.DEAD:
            self.updateAT()
            if self.currentAT == Unit.MAX_AT: self.canMove = True

    def updateAT (self):
        self.currentAT += self.speedCoeff()*self.SPEED/FPS
        if self.currentAT > Unit.MAX_AT:
            self.currentAT = Unit.MAX_AT

    def speedCoeff(self):
        if self.status == Battle.SLOW:
            return 1
        return 2
    
    def resetAT (self):
        self.currentAT = 0
        self.canMove = False
        
#----------------------------------------------------------------------------------------------
#Ability Definitions

#----------------------------------------------------------------------------------------------
#Move Definitions

voidMove = Move(None, None, None)
   
class Fight(Move): #Used for fight command
    def __init__(self):
        Move.__init__( self, 'Fight', 1, 0.9, isMagic = False)
fight = Fight()

class Potion(Move):
    def __init__(self):
        Move.__init__(self, 'Potion', 0, 1, damage = False)
    def moveEffect (self, user, target):
        Battle.num_Potion -= 1
        if self.canMoveEffect(user, target):
            if target.lastDamageTook[0] == '0':
                target.lastDamageTook[0] = str((int)(target.HEALTH- target.health))
                target.damageCount[0] = Unit.DAMAGECOUNTER
                target.damagecolor[0] = GREEN
            else:
                target.damageCount[1] = Unit.DAMAGECOUNTER
                target.lastDamageTook[1] = str((int)(target.HEALTH- target.health))
                target.damagecolor[1] = GREEN
            target.health = target.HEALTH
            Move.moveEffect(self, user, target)
        else:
            if target.lastDamageTook[0] == '0':
                target.lastDamageTook[0] = '10'
                target.damageCount[0] = Unit.DAMAGECOUNTER
                target.damagecolor[0] = GREEN
            else:
                target.damageCount[1] = Unit.DAMAGECOUNTER
                target.lastDamageTook[1] = '10'
                target.damagecolor[1] = GREEN
            target.health += 10
            Move.moveEffect(self, user, target)
    def canMoveEffect (self, user, target):
        return 10 + target.health >= target.HEALTH and target.status != Battle.DEAD
potionMove = Potion()

class Herb(Move):
    def __init__(self):
        Move.__init__(self, 'Herb', 0, 1, damage = False)
    def moveEffect (self, user, target):
        Battle.num_Herb -= 1
        if self.canMoveEffect(user, target):
            target.status = None
            Move.moveEffect(self, user, target)
    def canMoveEffect(self, user, target):
        return target.status != None and target.status != Battle.DEAD
herbMove = Herb()

class Elixer(Move):
    def __init__(self):
        Move.__init__(self, 'Elixer', 0, 1, damage = False)
    def moveEffect (self, user, target):
        Battle.num_Elixer -= 1
        if self.canMoveEffect(user, target):
            if target.lastDamageTook[0] == '0':
                target.lastDamageTook[0] = str((int)(target.MAGIC - target.magic))
                target.damageCount[0] = Unit.DAMAGECOUNTER
                target.damagecolor[0] = MANA_BLUE
            else:
                target.damageCount[1] = Unit.DAMAGECOUNTER
                target.lastDamageTook[1] = str((int)(target.MAGIC - target.magic))
                target.damagecolor[1] = MANA_BLUE
            target.magic = target.MAGIC
            Move.moveEffect(self, user, target)
        else:
            if target.lastDamageTook[0] == '0':
                target.lastDamageTook[0] = '10'
                target.damageCount[0] = Unit.DAMAGECOUNTER
                target.damagecolor[0] = MANA_BLUE
            else:
                target.damageCount[1] = Unit.DAMAGECOUNTER
                target.lastDamageTook[1] = '10'
                target.damagecolor[1] = MANA_BLUE
            target.magic += 10
            Move.moveEffect(self, user, target)
    def canMoveEffect (self, user, target):
        return 10 + target.magic >= target.MAGIC and target.status != Battle.DEAD
elixerMove = Elixer()

class Seal(Move):
    def __init__(self):
        Move.__init__(self, 'Seal', 0, 1, damage = False)
    def moveEffect (self, user, target):
        Battle.num_Seal -= 1
        if self.canMoveEffect(user, target):
            Move.moveEffect(self, user, target)
            target.status = None
            heal = ((int)((random.random()+0.5)*target.HEALTH/5))
            target.health = heal
            if target.lastDamageTook[0] == '0':
                target.lastDamageTook[0] = str(heal)
                target.damageCount[0] = Unit.DAMAGECOUNTER
                target.damagecolor[0] = GREEN
            else:
                target.damageCount[1] = Unit.DAMAGECOUNTER
                target.lastDamageTook[1] = str(heal)
                target.damagecolor[1] = GREEN
    def canMoveEffect(self, user, target):
        return target.status == Battle.DEAD
sealMove = Seal()

class MockingStrike(Move):
    def __init__(self):
        Move.__init__(self, 'Mocking Strike', 1, 1, 1, 5, isMagic = False) #0.8, 0.585,
    def moveEffect(self, user, target):
        execute = Move.moveEffect(self, user, target)
        if execute and self.canMoveEffect(user, target):
            target.status = Battle.SILENCE
    def canMoveEffect (self, user, target):
        return target.status == None and (random.random() < self.ACCURACY2)
mockingStrike= MockingStrike()

class Heal(Move):
    def __init__(self):
        Move.__init__(self, 'Heal', -2, 1, 1, 5, True, True, True)
heal = Heal()
    
#----------------------------------------------------------------------------------------------
#Monster Definitions

class Hamlet(Unit):
    def __init__ (self):
        Unit.__init__(self, 'Hamlet', [mockingStrike, heal, voidMove],
                      40.0, 10.0, 10, 2, 8,
                      5, 10, 15, 12, 12, 43,
                      pygame.image.load('hrassets/Hamlet/hamletstanding.png'),
                      pygame.image.load('hrassets/Hamlet/hamletidle.png'),
                      pygame.image.load('hrassets/Hamlet/hamletattack1.png'),
                      pygame.image.load('hrassets/Hamlet/hamletattack2.png'),
                      pygame.image.load('hrassets/Hamlet/hamletcast1.png'),
                      pygame.image.load('hrassets/Hamlet/hamletcast1.png'),
                      pygame.image.load('hrassets/Hamlet/hamletdead1.png'),
                      pygame.image.load('hrassets/Hamlet/hamletdead2.png'),
                      pygame.image.load('hrassets/Hamlet/hamletdead3.png'))

class Horatio(Unit):
    def __init__ (self):
        Unit.__init__(self, 'Horatio', [mockingStrike, heal, voidMove],
                      40.0, 10.0, 10, 2, 6,
                      5, 10, 20, 12, 22, 69,
                      pygame.image.load('hrassets/Horatio/horatiostanding.png'),
                      pygame.image.load('hrassets/Horatio/horatioidle.png'),
                      pygame.image.load('hrassets/Horatio/horatioattack1.png'),
                      pygame.image.load('hrassets/Horatio/horatioattack2.png'),
                      pygame.image.load('hrassets/Horatio/horatiocast1.png'),
                      pygame.image.load('hrassets/Horatio/horatiocast2.png'),
                      pygame.image.load('hrassets/Horatio/horatiodead1.png'),
                      pygame.image.load('hrassets/Horatio/horatiodead2.png'),
                      pygame.image.load('hrassets/Horatio/horatiodead3.png'))

class Ophelia(Unit):
    def __init__ (self):
        Unit.__init__(self, 'Ophelia', [mockingStrike, heal, voidMove],
                      40.0, 10.0, 10, 2, 10,
                      5, 10, 15, 12, 27, 83,
                      pygame.image.load('hrassets/Ophelia/opheliastanding.png'),
                      pygame.image.load('hrassets/Ophelia/opheliaidle.png'),                      
                      pygame.image.load('hrassets/Ophelia/opheliaattack1.png'),
                      pygame.image.load('hrassets/Ophelia/opheliaattack2.png'),
                      pygame.image.load('hrassets/Ophelia/opheliacast1.png'),
                      pygame.image.load('hrassets/Ophelia/opheliacast2.png'),
                      pygame.image.load('hrassets/Ophelia/opheliadead1.png'),
                      pygame.image.load('hrassets/Ophelia/opheliadead2.png'),
                      pygame.image.load('hrassets/Ophelia/opheliadead3.png'))
class Slime(Unit):
    def  __init__ (self):
        Unit.__init__(  self, 'Slime', [fight, fight, fight, fight],
                              20.0, 0.0, 4, 2, 6,
                              5, 10, 19, 10, 19, random.randint(30, 70),
                              slimeimg1, slimeimg2, slimeimg3, slimeimg4, slimeimg5,slimeimg6, slimeimg7, slimeimg8, slimeimg9)
        
slimeimg1 = pygame.image.load('hrassets/Slime/slimestanding.png')
slimeimg2 = pygame.image.load('hrassets/Slime/slimeidle.png')
slimeimg3 = pygame.image.load('hrassets/Slime/slimeattack1.png')
slimeimg4 = pygame.image.load('hrassets/Slime/slimeattack2.png')
slimeimg5 = pygame.image.load('hrassets/Slime/slimestanding.png')
slimeimg6 = pygame.image.load('hrassets/Slime/slimeidle.png')
slimeimg7 = pygame.image.load('hrassets/Slime/slimedead1.png')
slimeimg8 = pygame.image.load('hrassets/Slime/slimedead2.png')
slimeimg9 = pygame.image.load('hrassets/Slime/slimedead3.png')

#----------------------------------------------------------------------------------------------
#main pygame loop
def main():
    
    party = [Horatio(), Hamlet(), Ophelia()]
    enemies = [Slime(), Slime(), Slime()]
    battle = Battle(pygame.image.load('hrassets/bg1.png'), party, enemies) 
    battle.startBattle()
    
    pygame.quit()
    sys.exit()

main()
