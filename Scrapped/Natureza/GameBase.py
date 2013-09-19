""" Holds the basic inheritable classes and framework for the game """
from sfml import *

class Entity:
    """
    Represents an entity, holds specific sprites and internal logics
    that must be ran/drawn every tick. Entity is not an interface,
    as it is reasonable that there are classes that might not do
    anything and just want to be drawn somewhere
    """

    def __init__(self, window, sprite, drawPosition, parentModule):
        self.sprite = sprite
        self.window = window
        self.drawPosition = drawPosition
        self.parentModule = parentModule
        self.active = False

    def tick(self):
        """ A logical tick, runs internal logic. """
        
    def draw(self):
        """ Draws self on window. """
        self.window.draw(self.sprite)

class Module: 
    """
    Represents either a menu or a game mode, but it will be given
    controls that it can use, it will check every control it can use
    and then react appropriately based on those controls. It checks
    interactions between any entity within it (if it can interact)
    and then it runs the invidual logic of each entity
    """

    def __init__(self, window, textures):
        self.textures = textures
        # The list of lists structure is to create the ability to set priorities
        self.entities = [list()]
        self.controls = dict()
        self.window = window
        self.active = False

    def logic(self):
        """
        Modules runs its internal logic, mediating interactions between
        entities, at the end, it makes each entity run its internal logic
        """

        raise NotImplementedError("Class must implement logic(self)")

    def graphic(self):
        """ Draws any module specific stuff, then draws all entity stuff """

        raise NotImplementedError("Class must implement graphic(self)")

    def assignControl(self, control):
        """
        If this module uses this control, return true, and
        add it in, otherwise, return false and don't add it
        Most classes should never do this any differently
        """

        if self.controls.has_key(control):
            self.controls[control] = True
            return True
        return False

class Engine:
    """
    Highest level controller, will switch between different Modules,
    sometimes, we'll need multiple modules, but mostly we'll only be
    running one, alternate modules could be secondary game modes or
    menus, basically, the engine has to decide what will get the ability
    to utilize controls
    """
    STD_WIN_SIZE = (900, 600)
    
    def __init__(self):
        self.window = RenderWindow(VideoMode(Engine.STD_WIN_SIZE[0], Engine.STD_WIN_SIZE[1]), "Test")
        self.modules = [list()]
        self.controls = dict()
        self.textures = dict()
        
    def logics(self):
        """ Assigns controls to modules and runs all their logics """
        raise NotImplementedError("Class must implement logics(self)")

    def graphics(self):
        """ Assigns controls to modules and runs all their logics """
        raise NotImplementedError("Class must implement graphics(self)")

    def handleEvents(self):
        """
        Standard event handling, I won't use events for controls,
        so this will only relate to screen events
        """
        for event in self.window.events:
           if type(event) is CloseEvent:
              self.window.close()

           if type(event) is KeyEvent and event.code is Keyboard.ESCAPE:
              self.window.close()

    def run(self):
        while self.window.is_open:
            self.graphics()
            self.handleEvents()
            self.logics()

def test():
    """ Just checks to see if the constructors don't explode, if the window opens right and we draw the
        sprite, the test is good."""

    print("When manually running, check to see if the little tree appears")
    
    e = Engine()
    e.textures["pine 1"] = Texture.from_file("./Textures/tree_pine1.png")
    e.modules[0].append(Module(e.window, e.textures))
    e.modules[0][0].entities[0].append(Entity(e.window, Sprite(e.textures["pine 1"]), Vector2(0,0), e.modules[0][0]))

    e.modules[0][0].entities[0][0].draw()

    e.window.display()

    print("No problems running, check for the picture. Esc to end the test.")

    count = 0

    while(e.window.is_open or count < 200):
        count+=1
        for event in e.window.events:
            if type(event) is CloseEvent:
                e.window.close()

            if type(event) is KeyEvent and event.code is Keyboard.ESCAPE:
                e.window.close()

    return True

if __name__ == "__main__":
    test()
            
        
