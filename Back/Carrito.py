from __init__ import *

class Carrito(BaseModel):
    iden = PrimaryKeyField()
    total = DecimalField()
    cliente = ForeignKeyField(Cliente, backref='carrito')

    def getiden(self):
        return self.iden
    def setiden(self,new):
        self.iden = new

    def gettotal(self):
        return self.total
    def settotal(self,new):
        self.total = new

    def getcliente(self):
        return self.cliente
    def setcliente(self,new):
        self.cliente = new