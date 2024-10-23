from __init__ import *
# clase intermedia que relaciona carrito y producto
 
class CarritoProducto(BaseModel):
    carrito = ForeignKeyField(Carrito, backref='productos')
    producto = ForeignKeyField(Producto, backref='carritos')
    cantidad = IntegerField()

    def gatcarrito(self):
        return self.carrito
    def setcarrito(self,new):
        self.carrito = new

    def getproducto(self):
        return self.producto
    def setprodcuto(self,new):
        self.producto = new

    def getcantidad(self):
        return self.cantidad
    def setcantidad(self,new):
        self.cantidad = new