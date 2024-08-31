from __init__ import *

class Categoria(BaseModel):
    iden = PrimaryKeyField()
    nombre = CharField()

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def getnombre(self):
        return self.nombre
    def setnombre(self, new):
        self.nombre = new