class Inspectable:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def inspect(self):
        """ Return information on self """
        raise NotImplementedError("inspect() not implemented")
