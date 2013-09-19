from GameBase import *
import Natureza

from sfml import *

class NaturezaEngine (Engine):
    """ Overrides the Engine interface """
    def loadControls(self):
        """
        Add all game keys to controls dict, the
        value of the dict currently indicates the
        position in the module where the control
        was assigned
        """
        self.controls["up"] = -1
        self.controls["down"] = -1
        self.controls["left"] = -1
        self.controls["right"] = -1
        self.controls["q"] = -1
        self.controls["w"] = -1
        self.controls["e"] = -1
        self.controls["r"] = -1
        self.controls["t"] = -1
        self.controls["y"] = -1
        self.controls["u"] = -1
        self.controls["i"] = -1
        self.controls["o"] = -1
        self.controls["p"] = -1
        self.controls["["] = -1
        self.controls["]"] = -1
        self.controls["tab"] = -1
        self.controls["shift"] = -1
        self.controls["a"] = -1
        self.controls["s"] = -1
        self.controls["d"] = -1
        self.controls["f"] = -1
        self.controls["g"] = -1
        self.controls["h"] = -1
        self.controls["j"] = -1
        self.controls["k"] = -1
        self.controls["l"] = -1
        self.controls[";"] = -1
        self.controls["'"] = -1
        self.controls["return"] = -1
        self.controls["z"] = -1
        self.controls["x"] = -1
        self.controls["c"] = -1
        self.controls["v"] = -1
        self.controls["b"] = -1
        self.controls["n"] = -1
        self.controls["m"] = -1
        self.controls[","] = -1
        self.controls["."] = -1
        self.controls["/"] = -1
        self.controls["ctrl"] = -1
        self.controls["alt"] = -1
        self.controls["space"] = -1
        self.controls["`"] = -1
        self.controls["1"] = -1
        self.controls["2"] = -1
        self.controls["3"] = -1
        self.controls["4"] = -1
        self.controls["5"] = -1
        self.controls["6"] = -1
        self.controls["7"] = -1
        self.controls["8"] = -1
        self.controls["9"] = -1
        self.controls["0"] = -1
        self.controls["mouse"] = -1
        self.paused = False

    def loadTextures(self):
        try:
            self.textures["default_ground"] = Texture.from_file(
                "Textures/default_ground.png")
            self.textures["lion_male"] = Texture.from_file(
                "Textures/lion_male.png")
            self.textures["tree_pine1"] = Texture.from_file(
                "Textures/tree_pine1.png")

        except IOError:
            print("IOError! Some file not found")
    
    def __init__(self):
        Engine.__init__(self)
        self.loadControls()
        self.loadTextures()
        self.window.recreate(Natureza.VIDEOMODE(), "Natureza", Style.TITLEBAR)
        
    def logics(self):
        """ Assigns controls to modules and runs all their logics """
        if not self.paused:
            # Attempts to assign a control to every module based
            # on their position on the line, highest priority modules
            # will always get control of what they want
            controls = self.controls.keys()
            for control in controls:
                assigned = False
                position = -1
                while not assigned and position < len(self.modules) - 1:
                    position += 1
                    assigned = self.modules[position].assignControl(control)
                self.controls[control] = position
                    
            if (len(self.modules) > 0):
                for module in self.modules:
                    module.logic()

            # Reclaim all controls for the next cycle
            for control in controls:
                if self.controls[control] >= 0:
                    self.modules[self.controls[control]].controls[control] = False
                    self.controls[control] = -1
            
    def graphics(self):
        """ Assigns controls to modules and runs all their logics """
        self.window.clear()
        
        if not self.paused and len(self.modules) > 0:
            for module in self.modules:
                module.graphic()
                
        self.window.display()

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
    print("No test exists.")
    
if __name__ == "__main__":
    test()
