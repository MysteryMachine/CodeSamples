from GameBase import Entity
from RoguelikeActor import Actor
from RoguelikeActionable import *
from RoguelikeBuffable import Buffable
from RoguelikeStatsable import Statsable
from RoguelikeMapModuleBase import TileMappable

class UnitEntity(Entity, Statsable, TileMappable, Actor, Inspectable, Buffable):
    FAIL_AT = 10
    BASE_MAGDEF = 5.5
    WEIGHT_COEFF = 10
    HEALTH_COEFF = 19
    HREGEN_COEFF = 0.03
    ASPEED_COEFF = 1
    ARMOR_COEFF = 0.14
    MANA_COEFF = 13
    MREGEN_COEFF = 0.04
    MIN_ATKSPD = 15
    MIN_MVSPD = 0
    
    def __init__(self, window, sprite, parentModule):
        """ A very generic intialization, most characters will override """
        Statsable.__init__(self)
        Inspectable.__init__(self, "None", "None")
        Buffable.__init__(self)
        TileMappable.__init__(self)
        Entity.__init__(self, window, sprite, Vector2(0,0), parentModule)

        self.manaCurrent = self.mana

        self.__baseStrength__ = 0
        self.__baseAgilty__ = 0
        self.__baseIntelligence__ = 0

        self.__growthStrength__ = 0
        self.__growthAgility__ = 0
        self.__growthIntelligence__ = 0

        self.__baseMoveSpeed__ = 0
        self.__baseAttackSpeed__ = 0
            
        self.baseHungerLoss = 1
        self.currentHunger = 100
        
        self.slots = dict()
        self.items = list()

        self.brand = None

        self.updateStats()

    def updateStats(self):
        self.strength = self.__baseStrength__ + self.bonusStrength()
        self.intelligence = self.__baseIntelligence__ + self.bonusIntelligence()
        self.agility = self.__baseAgility__ + self.bonuseAgility()

        percentLeft = self.healthCurrent/self.health
        
        self.health = self.strength*UnitEntity.HEALTH_COEFF + self.bonusHealth()
        self.healthCurrent = self.health*percentLeft
        self.hRegen = self.strength*UnitEntity.HREGEN_COEFF + self.bonusHRegen()

        percentLeft = self.manaCurrent/self.mana
        
        self.mana = self.intelligence*UnitEntity.MANA_COEFF + self.bonusMana()
        self.manaCurrent = percentLeft*self.mana
        self.mRegen = self.intelligence*UnitEntity.MREGEN_COEFF + self.bonusMRegen()
        
        self.armor = self.agility*UnitEntity.ARMOR_COEFF + self.bonusArmor()
        self.magicArmor = UnityEntity.BASE_MAGDEF + self.bonusMagicArmor()

        self.weight = self.strength*UnitEntity.WEIGHT_COEFF + self.bonusWeight()
        self.currentWeight = self.currentWeight()
        self.moveSpeed =  self.moveSpeed()
        self.speed = self.moveSpeed
        self.attackSpeed = self.__baseAttackSpeed__ - self.agility*UnitEntity.ASPEED_COEFF - self.bonusAttackSpeed
        
        self.bonusDamage = self.bonusDamage()
        
    def levelUp(self):
        self.level += 1
        self.experience = 0
        
        self.__baseStrength__ += self.__growthStrength___
        self.__baseIntelligence__ += self.__growthIntelligence__
        self.__baseAgility__ += self.__growthAgility__

        self.updateStats()

    def bonusStrength(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].strength

        for buff in buffs:
            bonus += buff.strength

        return bonus
    
    def bonusAgility(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].agility

        for buff in buffs:
            bonus += buff.agility
            
        return bonus

    def bonusIntelligence(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].intelligence

        for buff in buffs:
            bonus += buff.intelligence
            
        return bonus

    def bonusArmor(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].armor

        for buff in buffs:
            bonus += buff.armor
            
        return bonus

    def bonusMagicArmor(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].magicArmor

        for buff in buffs:
            bonus += buff.magicArmor
            
        return bonus
    
    def bonusHealth(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].health

        for buff in buffs:
            bonus += buff.health
            
        return bonus

    def bonusMana(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].mana

        for buff in buffs:
            bonus += buff.mana
            
        return bonus

    def bonusHRegen(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].hRegen

        for buff in buffs:
            bonus += buff.hRegen
            
        return bonus

    def bonusMRegen(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].mRegen

        for buff in buffs:
            bonus += buff.mRegen
            
        return bonus

    def bonusWeight(self):
        bonus = 0
        keys = slots.keys()

        for buff in buffs:
            bonus += buff.weight
            
        return bonus

    def bonusCurrentWeight(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].currentWeight

        for buff in buffs:
            bonus += buff.currentWeight
            
        return bonus

    def attackSpeed(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].attackSpeed

        for buff in buffs:
            bonus += buff.attackSpeed
            
        total = self.__baseAttackSpeed__ - bonus

        if total < UnitEntity.MIN_ATKSPD:
            total = UnityEntity.MIN_ATKSPD

        return total

    def moveSpeed(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].moveSpeed

        for buff in buffs:
            bonus += buff.moveSpeed

        total = self.__baseMoveSpeed__ - bonus

        if total < UnitEntity.MIN_MVSPD:
            total = UnityEntity.MIN_MVSPD
            
        return total

    def bonusDamage(self):
        bonus = 0
        keys = slots.keys()

        for key in keys:
            bonus += slots[key].bonusDamage

        for buff in buffs:
            bonus += buff.bonusDamage
            
        return bonus
