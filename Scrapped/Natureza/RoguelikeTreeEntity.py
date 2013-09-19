"""
This file will hold the base class of all the trees in the game
"""

from GameBase import Entity
from GameBaseActionable import Inspectable
from GameBaseDamageable import Damageable
from RoguelikeMapModuleBase import *

class TreeEntity (Entity, Inspectable, Damageable):
""" A basic parent class for tree functionality """
    def getTypeString(self):
        if(self.treeType == "tree_pine1"):
            return "Pine Tree"
        else:
            print("Tree type undefined")
            raise ValueError()
        
    def __init__(self, window, textures, position, parentModule,
                 treeType, mature = True, maturationTime = 0, fruitType = None):
        if(not isinstance(parentModule, MapModuleBase))
            print("Tree's parent module not a map module. Plants should only exist on Map Modules")
            raise TypeError()
        
        if(mature):
            sprite = Sprite(textures[treeType])
        else:
            sprite = Sprite(textures["tree_sapling"])
        
        self.treeType = treeType

        # Growth code
        if(mature):
            self.timeToMaturity = 0
        else:
            self.timeToMaturity = maturationTime

        # Fruit tree handling code            
        if(fruitType is not None and type(fruitType) is Fruit):
            self.fruitType = fruitType
            self.fruitBearing = True
            self.hasFruit = False
            self.fruitTimer = fruitType.growTime
        else:
            self.fruitBearing = False
            self.fruitType = None
            self.hasFruit = False
            self.fruitTimer = -1
        
        GameBase.Entity.__init__(self, window, sprite, position, parentModule)

    def tick(self):
        """ Calculates growth of fruits and the tree """
        # Tree growth code
        if (not self.mature):
            self.timeToMaturity -= self.parentModule.map[position.x][position.y].fertility
            
        if(self.fruitBearing and not self.hasFruit and self.fruitTimer is not 0):
            self.fruitTimer -= self.parentModule.map[position.x][position.y].fertility
            if(self.fruitTimer <= 0):
                self.hasFruit = True
                self.fruitTimer = 0
        elif(self.fruitBearing and not self.hasFruit and self.fruitTimer is 0):
            self.fruitTimer =  self.fruitType.growTime

    def inspect(self):
        raise NotImplementedError("inspect()")

    def die(self):
        raise NotImplementedError("die()")

    def draw(self):
        raise NotImplementedError("draw()")

def test():
    print("No test")

if __name__ == "__main__":
    test()
