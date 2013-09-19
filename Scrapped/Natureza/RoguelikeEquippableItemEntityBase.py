from RoguelikeItemEntityBase import ItemEntityBase
from RoguelikeActionable import Evokable
from RoguelikeActionable import Aurable
from RoguelikeUnitEntityBase import Statsable

class EquippableItemEntityBase (ItemEntityBase, Statsable, Evokable):
    """ Base class for equippable items in a roguelike, items made
        should inherit from this if they need to implement specific
        functionality, building items through inheritence is probably
        the smartest thing in any instance"""
    def __init__(self, window, sprite, drawPosition, parentModule, 
                owner, weight, value, name, description, useTime, slots, strength = 0, 
                intelligence = 0, agility = 0,  health = 0  hreg = 0, 
                mana = 0, mreg = 0, armor = 0, magicArmor = 0, bdam = 0, brand = None
                mvspd = 0, aspd = 0, cweight = 0, buff = None,
                aura = None, evokeStyle = Evokable.self):
        ItemEntityBase.__init__(self, window, sprite, drawPosition, parentModule,
                owner, weight, value, name, description, useTime)
        Evokable.__init__(self, buff, evokeStyle)
        Statsable.__init__(self)
        
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        
        self.health = health
        self.hRegen = hreg
        
        self.mana = mana
        self.mRegen = mreg
        
        self.armor = armor
        self.magicArmor = magicArmor

        self.currentWeight = weight
        
        self.moveSpeed = mvspd
        self.attackSpeed = aspd

        self.slots = slots

        self.bonusDamage = bdam

        self.brand = brand
        
    def tick(self):
        return

    def evoke(self):
        Buffable.buff(self.owner, self.buff)
