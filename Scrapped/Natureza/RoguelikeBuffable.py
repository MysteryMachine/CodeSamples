import copy

from RoguelikeStatsable import Statsable

class Buff(Statsable):
    def __init__(self, duration, strength = 0, mvspd = 0, aspd = 0,
                intelligence = 0, agility = 0,  health = 0,  hreg = 0, 
                mana = 0, mreg = 0, armor = 0, magicArmor = 0, bdam = 0,
                cweight = None, specialID = None):
        Statsable.__init__(self)

        self.duration = duration
        
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        
        self.health = health
        self.hRegen = hreg
        
        self.mana = mana
        self.mRegen = mreg
        
        self.armor = armor
        self.magicArmor = magicArmor

        self.weight = weight
        self.currentWeight = cweight
        self.moveSpeed = mvspd
        self.attackSpeed = aspd

        self.slots = slots

        self.bonusDamage = bdam
        
        self.specialID = specialID

    def tick(self):
        if self.duration > 0:
            self.duration -= 1
    
class Buffable:
    def __init__(self):
        self.buffs = list()
                 
    def buff(target, buff):
        if isinstance(target, Buffable):
            target.buffs.append(copy.deepcopy(buff))
            return True
        else:
            return False

    def tickBuffs(self):
        if len(self.buffs > 0):
            for i in range(len(self.buffs)):
                self.buffs[i].tick()
                if buff.duration == 0:
                    self.buffs.pop(i)
