""" This file contains some basic or otherwise miscellaneous functions required
    in a roguelike. Right now, only the Actor class is there. """

from GameBase import Entity

class Actor:
    """ This class contains a list of useable actions, and will only add an
        action to a list of the instance of Actor is a member of the proper
        class """
    def __init__(self):
        if not(isinstance(self, Entity)):
            # Meant to avoid diamonds
            raise TypeError("Cannot inheret Actor if it is not an instance of Entity")
        self.currentActionIndex = -1
        self.interrupted = False
        self.failedMoves = 0
        self.failedToMove = False
        self.nextAction = None
        self.actionTime = 0

    def done(self):
        self.nextAction = None
        self.interrupted = False
        self.failedMoves = 0
        self.currentActionIndex = -1
        self.actionTime = 0
