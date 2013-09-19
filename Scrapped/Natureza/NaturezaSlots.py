""" Has general slots returns for various kinds of creatures in Natureza """

class Slots:
    """ Functions for returning equippable slots """
    LEFT_HAND = "Left Hand"
    RIGHT_HAND = "Right Hand"
    MOUTH-E = "Weapon Holding Mouth"
    HEAD = "Head"
    HEAD-D = "Deformed Head"
    BODY = "Body"
    BODY-D = "Deformed Body"
    BODY-Q = "Quadruped Body"
    FEET-D = "Deformed Feet"
    FEET = "Feet"
    RING_1 = "Ring 1"
    RING_2 = "Ring 2"
    RING_3 = "Ring 3"
    RING_4 = "Ring 4"
    AMULET_1 = "Amulet 1"
    AMULET_2 = "Amulet 2"
    
    def getHumanoidSlots():
        slots = dict()
        slots[Slots.LEFT_HAND] = 0
        slots[Slots.RIGHT_HAND] = 0
        slots[Slots.HEAD] = 0
        slots[Slots.BODY] = 0
        slots[Slots.FEET] = 0
        slots[Slots.RING_1] = 0
        slots[Slots.RING_2] = 0
        slots[Slots.AMULET_1] = 0

        return slots

    def getHugeHumanoidSlots():
        slots = dict()
        slots[Slots.LEFT_HAND] = 0
        slots[Slots.RIGHT_HAND] = 0
        slots[Slots.HEAD-D] = 0
        slots[Slots.BODY-D] = 0
        slots[Slots.FEET-D] = 0
        slots[Slots.RING_1] = 0
        slots[Slots.RING_2] = 0
        slots[Slots.AMULET_1] = 0

        return slots

    def getOgreSlots():
        slots = Slots.getHugeHumanoidSlots()
        slots[Slots.AMULET_2] = 0

        return slots

    def getQuadrupedSlots():
        slots = dict()
        slots[Slots.MOUTH-E] = 0
        slots[Slots.BODY-Q] = 0
        slots[Slots.RING_1] = 0
        slots[Slots.RING_2] = 0
        slots[Slots.RING_3] = 0
        slots[Slots.RING_4] = 0
        slots[Slots.AMULET_1] = 0

        return slots

    def getFairySlots():
        slots = dict()
        slots[Slots.RING_1] = 0
        slots[Slots.RING_2] = 0
        slots[Slots.RING_3] = 0
        slots[Slots.RING_4] = 0
        slots[Slots.AMULET_1] = 0

        return slots
