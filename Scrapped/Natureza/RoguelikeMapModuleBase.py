""" This file contains the Tile class, The TileMapModuleBase class, and the TileMapModuleMover
    All these classes rely on each other, and require each other"""
import GameBase
from RoguelikeActor import Actor
import copy
import random

from sfml import *

class TileMoveType:
    IMPASSIBLE = 0
    NORMAL = 1
    DIFFICULT = 2
    SHALLOW = 3
    WATER = 4
    SOLID = 5
    LAVA = 6

    TOTALTYPES = 7

    def toString(element):
        if(element is WalkTileMove.IMPASSIBLE):
            return "Impassible"
        elif(element is WalkTileMove.NORMAL):
            return "Normal"
        elif(element is WalkTileMove.DIFFICULT):
            return "Difficult"
        elif(element is WalkTileMove.SHALLOW):
            return "Shallow"
        elif(element is WalkTileMove.WATER):
            return "Water"
        elif(element is WalkTileMove.SOLID):
            return "Solid"
        elif(element is WalkTileMove.LAVA):
            return "Lava"
        else:
            print(element)
            raise TypeError("GroundType undefined")
        
    def delay(element):
        """ Returns base delay of moving into this tile """
        if(element is WalkTileMove.IMPASSIBLE):
            return 0
        elif(element is WalkTileMove.NORMAL):
            return 10
        elif(element is WalkTileMove.DIFFICULT):
            return 25
        elif(element is WalkTileMove.SHALLOW):
            return 35
        elif(element is WalkTileMove.WATER):
            return 50
        elif(element is WalkTileMove.SOLID):
            return 100
        elif(element is WalkTileMove.LAVA):
            return 90
        else:
            print(element)
            raise TypeError("GroundType undefined")
class Tile:
    """ Class relating to map tiles and their information """
    FAILEDMOVEDELAY = 1
    
    def __init__(self, texture, groundType, position):
        self.sprite = Sprite(texture)
        self.sprite.position = position
        self.moveType = moveType
        self.fertility = 1
        self.entity = None
        self.items = list()
        self.cloudEntity = None
        self.traversableEntity = None

class TileMapModuleBase (GameBase.Module):
    DIAGONAL_COEFF = 1.41421 #~sqrt(2)
    
    def __init__(self, mapSize, tileSize, window, textures):
        GameBase.Module.__init__(self, window, textures)
        self.size = mapSize
        self.tileSize = tileSize
        self.draqRequest = False
        self.pileTexture = textures["item_pile.png"]
        
        self.map = [[[]for i in range(mapSize)] for i in range(mapSize)]

    def graphic(self):
        """ Draws every map tile first, then draws the entities """

        for row in self.map:
            for tile in row:
                self.window.draw(tile.sprite)
                if not tile.entity == None:
                    if not tile.cloudEntity == None:
                        self.window.draw(tile.cloudEntity.sprite)
                    elif not tile.traversableEntity == None:
                        self.window.draw(tile.traversableEntity.sprite)
                    elif len(tile.items) > 0:
                        if len(self.items) > 2:
                            sprite = Sprite(self.pileTexture)
                            sprite.position = tile.sprite.position
                            self.window.draw(sprite)
                        else:
                            self.window.draw(tile.items[0].sprite)

    def logic(self):
        """ The base map has no behavior """
        return 0

class TileMappable:
    """ Any entity that can be mapped on a tilemap inherets these properties """
    def __init__(self, initPosition = Vector2(0, 0), movecoeffs = [1, 1, 1, 1, 1, 1, 1,], speed = 0, failTolerance = 10):
        if(not isinstance(self, GameBase.Entity) and not isinstance(self.parentModule, TileModuleBase))\
               and not isinstance(self, Actor):
            raise TypeError("Only actor Entities who parents are a tilemodulebase may be tilemappable")
        self.tileMapPosition = initPosition
        if(not len(movescoeffs) == GroudType.TOTALTYPES):
            raise TypeError("Movespeeds list is not the correct size")
        self.movecoeffs = movecoeffs
        self.MOVECOEFFS = copy.deepcopy(movecoeffs)
        self.randMove = False
        self.path = None
        self.speed = speed
        self.failTolerance = failTolerance

    def setPath(self, destination, quick = True):
        """ Use's Dijsktra's algorithm to search for a path to the destination, anytime quick is true, it
            just returns the first path found, regardless of speed """
        # initialize the map
        timeMap = [[[]for i in range(self.parentModule.size)] for i in range(self.parentModule.size)]
        for i in range(0, self.parentModule.size):
            for j in range(0, parentModule.size):
                timeMap[i][j] = [0, self.getAT(Vector2(i, j)), [list(), list()], [i, j]]
                if timeMap[i][j][1] < 0 or self.parentModule.map[i][j].entity == None:
                    timeMap[i][j][0] = -1

        timeMap[self.tileMapPosition.x][self.tileMapPosition.y] = [0, 0, [list(), list()], [self.tileMapPosition.x, self.tileMapPosition.y]]
        #timemap[x][y][0] is distance from start
        #[1] is the time it takes to walk onto that tiles
        # is the list of positions that most quickly lead to that path, and a list of the times to walk on each of those postions
        # the past place is the location x,y of the tile

        queue = [timeMap[self.tileMapPosition.x][self.tileMapPosition.y]]

        quickNotDone = True
        
        while(not len(queue) and quickNotDone):
            item = queue.pop()
            for i in range(-1, 1, 2):
                for j in range (-1, 1, 2):
                    if not i == 0 and not j == 0:
                        # Calculate coordinates of adjacant squares
                        x = i + item[3][0]
                        y = item[3][1] + j
                        V = Vector2(x, y)
                        # Check to see if we are in bounds
                        if(x >= 0 and x < len(timeMap) and y >= 0 and y < len(timeMap)):
                            nVal = timeMap[i][j][0] + timeMap[x][y][0]
                            # Take diagonality into account
                            if(not x == 0 and not y ==0 ):
                                nVal*=TileMapModuleBase.DIAGONAL_COEFF
                            # If this is the smallest distance yet
                            if (nVal < timeMap[x][y][0] or timeMap[x][y][0] <= 0):
                                timeMap[x][y][0] = nVal
                                # Copy in the new path
                                timeMap[x][y][2] = copy.deepcopy(timeMap[i][j][2])
                                timeMap[x][y][2][0].append(V)
                                timeMap[x][y][2][1].append(timeMap[x][y][1])
                                if(quick and x == destination.x and y == destination.y):
                                    return timeMap(timeMap[destination.x][destination.y][2])

        return timeMap(timeMap[destination.x][destination.y][2])
    
    def getAT(self, path):
        """ Multiply the delay of the tile by the parentActorEntity's movecoeffecient for that type of ground """
        base = TileMoveType.delay(self.parentModule.map[path.x][path.y].groundType)
        coeff = self.movecoeff[parentActorEntity.parentModule.map[path.x][path.y].groundType]
        return base*coeff // 1   

        
    def move(self, target = None, makepath = True, fastPath = True):
        """ Checks to see if the previously calculated path works, still, or moves randomly, and if it still does
            it pops off the previous path and calls the base do """
        # Get path and action time

        path = None
        
        if target is not None and makePath:
            self.setPath(target.destination, fastPath)
            target = None
        
        if target is None:
            if en(self.parentActorEntity.path) > 0 and not randMove:
                path, actionTime = self.path[0][0], self.path[1][0]

        elif not target is None and not makepath:
            path = target.destination
            self.actionTime = target.actionTime
                
        elif self.randMove:
            path = Vector2(randint(-1, 1), randint(-1, 1))
            self.actionTime = self.parentActorEntity.getAT(path)
        # Check the validity of the action
        if not self.parentModule.map[path.x][path.y].entity is None or self.actionTime <= 0 or path is None:
            self.failedMoves += 1
            self.actionTime = TileMappable.FAILEDMOVEDELAY
            self.failedToMove = True
        else:
            self.failedMoves = 0

        # For simplicity's sake, for now, we're moving and THEN taking the time to move,
        # this will be basically unseeable to the player
        if not self.failedToMove:
            self.tileMapPosition = path
            self.map[path.x][path.y].entity = self
                       
            if not self.randMove and target is None:
                self.path[0].pop()
                self.path[1].pop()

        self.nextAction = TileMappable.__keepMoving__
        
    def __keepMoving__(self):        
        self.actionTime -= self.speed
        if(self.interrupted or (self.actionTime <= 0 and self.failedToMove == False)):
            self.done()
        # If pathing to an area, give it another couple of tries before quitting and repathing
        elif(self.actionTime <= 0 and self.failTolerance > self.failedMoves and len(self.path) > 0):
            self.failedToMove = False
            self.nextAction = TileMappable.move
        # If you can't do it after trying a few more times (whatever is in the way isn't budging), be done and
        # have the entity decide on a new action to undertake
        elif(self.actionTime <= 0 and self.failTolerance <= self.failedMoves and len(self.path) > 0):
            self.done()
        else:
            self.nextAction = TileMappable.__keepMoving__
        
def test():
    print("Currently no test")
        
if __name__ == "__main__":
    test()
