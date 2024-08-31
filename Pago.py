from __init__ import *

class Pago(BaseModel):
    iden = PrimaryKeyField()
    total = DecimalField()
    metododepago = CharField()
    numerodetarjeta = CharField()
    estado = CharField()

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def gettotal(self):
        return self.total
    def settotal(self, new):
        self.total = new

    def getmetododepago(self):
        return self.metododepago
    def setmetododepago(self, new):
        self.metododepago = new

    def getnumerodetarjeta(self):
        return self.numerodetarjeta
    def setnumerodetarjeta(self, new):
        self.numerodetarjeta = new

    def getestado(self):
        return self.estado
    def setestado(self, new):
        self.estado = new