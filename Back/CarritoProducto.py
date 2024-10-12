from __init__ import *
#es una clase intermedia para hacer la relacion entre carrito y producto
 
class CarritoProducto(BaseModel): #
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