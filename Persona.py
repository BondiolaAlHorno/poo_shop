from __init__ import *

class Persona(BaseModel):
    iden = PrimaryKeyField()
    nombre = CharField()
    apellido = CharField()
    telefono = CharField()
    documento = CharField()
    mail = CharField()

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def getnombre(self):
        return self.nombre
    def setnombre(self, new):
        self.nombre = new

    def getapellido(self):
        return self.apellido
    def setapellido(self, new):
        self.apellido = new

    def gettelefono(self):
        return self.telefono
    def settelefono(self, new):
        self.telefono = new

    def getdocumento(self):
        return self.documento
    def setdocumento(self, new):
        self.documento = new

    def getmail(self):
        return self.mail
    def setmail(self, new):
        self.mail = new