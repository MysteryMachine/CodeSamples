from GameBaseDamageable import Damageable

class Statsable(Damageable):
    def __init__(self):
        Damageable.__init__(self)
        self.mana = 0
        
        self.strength = None
        self.agility = None
        self.intelligence = None

        self.level = 1
        self.experience = 0
        
        self.moveSpeed = None
        self.attackSpeed = None
        
        self.hRegen = None
        self.mRegen = None

        self.weight = None
        self.currentWeight = None

        self.bonusDamage = None
