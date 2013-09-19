class Attack:
    """ Meant to work with damagable, an Attack is a direct
        communication of what is being doing """
    def __init__(self, damage, attackType, element):     
        self.damage = damage
        self.attackType = attackType
        self.element = element

class Element:
    """ An enum for Element
        If reusing this code in the future, feel free
        too change around the list (though I likely won't,
        this is the element list I most enjoy in games"""
    FIRE = 0
    EARTH = 1
    WATER = 2
    WIND = 3
    LIGHT = 4
    DARK = 5

    LEN_ELEMENTS = 6

    def toString(element):
        if(element is Element.FIRE):
            return "Fire"
        elif(element is Element.EARTH):
            return "Earth"
        elif(element is Element.WATER):
            return "Water"
        elif(element is Element.WIND):
            return "Wind"
        elif(element is Element.LIGHT):
            return "Light"
        elif(element is Element.DARK):
            return "Dark"
        else:
            print ("Wrong element type")
            raise ValueError()

    def baseMatchups():
        return [1, 1, 1, 1, 1, 1]

class Damage:
    """ An enum for Damage
        when resuing attack, be sure to change up
        this enum's definition so that it reflects the
        kinds of damage you'll be utilizing """
    PHYSICAL = 0
    MAGICAL = 1
    MIXED = 2
    PURE = 3

    def toString(damage):
        if(damage is Damage.PHYSICAL):
            return "Physical"
        elif (damage is Damage.MAGICAL):
            return "Magical"
        elif (damage is Damage.MIXED):
            return "Mixed"
        elif (damage is Damage.PURE):
            return "Pure"
        else:
            raise ValueError()

class Damageable:
    """ Contains defensive stats along with the standard implementation
        for taking damage """
    DEFENSE_COEFFICIENT = 0.06
    def __init__(self, health = 0, armor = 0, magicArmor = 0):
        self.health = health
        self.currentHealth = health
        self.armor = armor
        self.magicArmor = magicArmor

        self.resists = Element.baseMatchups()
    
    def damage(self, attack):
        """ Applies damage to self based on an attack recieved """
        damage = attack.damage
        defense = 0
        if(attack.attackType is Damage.PHYSICAL):
            defense = self.armor
        elif(attack.attackType is Damage.MAGICAL):
            defense = self.magicArmor
        elif(attack.attackTpe is Damage.MIXED):
            defense = (self.magicArmor + self.zrmor)/2

        resist = self.resists[attack.element]

        damage *= resist*defense*DEFENSE_COEFFICIENT/(1+defense*DEFENSE_COEFFICIENT)

        self.health -= damage
        if(self.health <= 0):
            self.die()

    def die(self):
        raise NotImplementedError("Child class must implement death")

def test():
    print("No test exists.")
    
if __name__ == "__main__":
    test()
