from __init__ import *

class Cliente(Persona):
    direccion = CharField()

    def getdireccion(self):
        return self.direccion
    def setdireccion(self, new):
        self.direccion = new