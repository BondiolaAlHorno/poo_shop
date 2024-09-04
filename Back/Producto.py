from __init__ import *

class Producto(BaseModel):
    iden = PrimaryKeyField()
    descripcion = CharField(270)
    precio = DecimalField(10,2)
    stock = IntegerField()
    marca = CharField()
    modelo = CharField()

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def getdescripcion(self):
        return self.descripcion
    def setdescripcion(self, new):
        self.descripcion = new

    def getprecio(self):
        return self.precio
    def setprecio(self, new):
        self.precio = new

    def getstock(self):
        return self.stock
    def setstock(self, new):
        self.stock = new

    def getmarca(self):
        return self.marca
    def setmarca(self, new):
        self.marca = new

    def getmodelo(self):
        return self.modelo
    def setmodelo(self, new):
        self.modelo = new