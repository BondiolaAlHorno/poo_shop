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
    
    @classmethod
    def crear_carrito(cls, cliente):
        return cls.create(total=0, cliente=cliente)

    def anadir_producto_al_carrito(self, producto, cantidad):
        CarritoProducto.create(carrito=self, producto=producto, cantidad=cantidad)
        self.calcular_total()

    def modificar_carrito(self, producto, cantidad):
        carrito_producto = CarritoProducto.get_or_none(
            (CarritoProducto.carrito == self) & (CarritoProducto.producto == producto)
        )
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
        # Aca tendría que ir la lógica para confirmar el carrito
        pass

    def mostrar_carrito(self):
        return list(CarritoProducto.select().where(CarritoProducto.carrito == self))

    def calcular_total(self):
        total = sum(cp.producto.precio * cp.cantidad for cp in self.mostrar_carrito())
        self.total = total
        self.save()

    @classmethod
    def obtener_carrito_por_cliente(cls, cliente):
        return cls.get_or_none(cls.cliente == cliente)