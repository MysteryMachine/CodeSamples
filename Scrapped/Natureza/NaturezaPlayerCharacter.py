from RoguelikeUnitEntityBase import UnityEntity

class PlayerCharacter(UnitEntity):
    def __init__(self, window, sprite, parentModule):
        UnitEntity.__init__(self, window, sprite, parentModule):

    def tick(self):
        self.nextAction()
        self.tickBuffs()

    def draw(self):
        self.sprite.position = self.drawPosition
        self.window.(self.sprite)

    def inspect(self):
        return self.name
