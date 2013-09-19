""" Contains some basic and generic useful items and base items for a roguelike """

from GameBase import Entity
from RoguelikeActionable import Inspectable

class ItemEntityBase (Entity, Inspectable, Useable):
    """ Base class for items in the game """
    def __init__(self, window, sprite, drawPosition, parentModule, owner, weight, value, name, description, useTime):
        Entity.__init__(self, window, sprite, drawPosition, parentModule)
        Inspectable.__init__(self, name, description)
        self.weight = weight
        self.value = value
        self.owner = owner
        self.useTime = useTime

    def draw(self):
    """ Items shouldn't draw themselves, because they can be stepped over """
        return

    def tick(self):
    """ Generic items have no behavior """
        return

    def use(self, target):
        raise NotImplementedError("Child items should implement their own use function")

    def inspect(self):
        raise NotImplementedError("Haven't implemented inspect code yet")
    
class RottableItemEntityBase (ItemEntityBase):
    def __init__(self, window, sprite, drawPosition, parentModule, owner, weight, value, rotTime, name, description, useTime):
        ItemEntityBase.__init__(self, window, sprite, drawPosition, parentModule, owner, weight, value, name, description, useTime)
        self.rotTime = rotTime
        self.rotRate = 1

    def tick(self):
        """ When the rotTime reaches 0, the item rots """
        self.rotTime -= self.rotRate
        if self.rotTime <= 0:
            self.active = False

class Food (RottableItemEntityBase):
    def __init__(self, window, sprite, drawPosition, parentModule, owner, weight, value, rotTime, name, description, useTime, sickChance = 0):
        ItemEntityBase.__init__(self, window, sprite, drawPosition, parentModule, owner, weight, value, name, description, useTime)
        self.sickChance = sickChance

    def use(self, target):
        
        
class Corpse (RottableItemEntityBase):
    def __init__(self, window, sprite, drawPosition, parentModule, weight, owner, value, rotTime, chunks, chunkType, name, description, useTime):
        RottableItemEntityBase.__init__(self, window, sprite, drawPosition, parentModule, owner, weight, value, rotTime, name, description, useTime)
        self.chunks = chunks
        self.chunkType = chunkType

    def use(self):
        """ Butchers the corpse and drops chunks """
        self.active = False
        for i in range(0, self.chunks):
            owner.items.append(chunkType())
