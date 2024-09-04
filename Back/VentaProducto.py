from __init__ import *

class VentaProducto(BaseModel):
    venta = ForeignKeyField(Venta, backref='productos')
    producto = ForeignKeyField(Producto, backref='ventas')
    cantidad = IntegerField()

    def getventa(self):
        return self.venta
    def setventa(self,new):
        self.venta = new

    def getproducto(self):
        return self.producto
    def setproducto(self,new):
        self.producto = new
    
    def getcantidad(self):
        return self.cantidad
    def setcantidad(self,new):
        self.cantidad = new