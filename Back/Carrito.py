from __init__ import *

class Carrito(BaseModel):  #definimos la clase y pasamos los atributos que va a tener esta clase,  ide, total, cliente
    iden = PrimaryKeyField()
    total = DecimalField()
    cliente = ForeignKeyField(Cliente, backref='carrito') 
#le definimos los get y set a cada atributo
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
    
    def get_id_producto(self,producto):
        return producto.getiden()
    
    def get_descripcion_producto(self,producto):
        return producto.getdescripcion()
    
    def get_precio_producto(self,producto):
        return producto.getprecio()
    
    def get_stock_producto(self,producto):
        return producto.getstock()
    
    def get_marca_producto(self,producto):
        return producto.getmarca()
    
    def get_modelo_producto(self,producto):
        return producto.getmodelo()

    def anadir_producto_al_carrito(self, producto, cantidad):
        CarritoProducto.create(carrito=self, producto=producto, cantidad=cantidad)
        self.calcular_total()

    def modificar_carrito(self, producto, cantidad):
        carrito_producto = CarritoProducto.get_or_none((CarritoProducto.carrito == self) & (CarritoProducto.producto == producto))
        if carrito_producto:
            if cantidad > 0:
                carrito_producto.cantidad = cantidad
                carrito_producto.save()
            else:
                carrito_producto.delete_instance()
            self.calcular_total()
            return True
        return False

    def confirmar_carrito(self):
        # Aca tendria que ir la lógica para confirmar el carrito
        pass

    def mostrar_carrito(self):
        return self.productos

    def calcular_total(self):
        total = sum(item.producto.precio * item.cantidad for item in self.mostrar_carrito())
        self.total = total
        self.save()
        return self.total