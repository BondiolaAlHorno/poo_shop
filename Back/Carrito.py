from __init__ import *

class Carrito(BaseModel):
    iden = PrimaryKeyField()
    total = DecimalField()
    cliente = ForeignKeyField(Cliente, backref='carrito', unique=True) 

    def getiden(self):
        return self.iden

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

    # agrega un produto al carrito, se le pasa un producto y la cantidad del mismo
    def anadir_producto_al_carrito(self, producto:'Producto', cantidad:int):
        from CarritoProducto import CarritoProducto
        carrito_producto = CarritoProducto.get_or_none((CarritoProducto.carrito == self) & (CarritoProducto.producto == producto))
        if carrito_producto:
            carrito_producto.cantidad += cantidad
            carrito_producto.save()
        else:
            CarritoProducto.create(carrito=self, producto=producto, cantidad=cantidad)
        producto.setstock(producto.getstock()-cantidad)
        producto.save()
        self.calcular_total()

    # modifica la cantidad de un producto determinado en el carrito, se le pasa un producto y la cantidad
    def modificar_carrito(self, producto:'Producto', cantidad:int):
        from CarritoProducto import CarritoProducto
        carrito_producto = CarritoProducto.get_or_none((CarritoProducto.carrito == self) & (CarritoProducto.producto == producto))
        if carrito_producto:
            if cantidad > 0:
                producto.setstock(producto.getstock()+carrito_producto.cantidad-cantidad)
                producto.save()
                carrito_producto.cantidad = cantidad
                carrito_producto.save()
            else:
                producto.setstock(producto.getstock()+carrito_producto.cantidad-cantidad)
                producto.save()
                carrito_producto.delete_instance()
            self.calcular_total()
            return True
        return False

    # confirma la seleccion de productos en el carrito y crea un objeto Venta con los productos del carrito
    def confirmar_carrito(self,fecha:str,envio:float):
        from VentaProducto import VentaProducto
        from Venta import Venta
        with getdatabase().atomic():
            venta = Venta.create(
                estado = 'Pendiente',
                fecha = fecha,
                envio = envio,
                total = self.total,
                cliente = self.cliente
            )
            [VentaProducto.create(venta=venta,producto=item.producto,cantidad=item.cantidad) for item in self.productos]
        return venta

    # devuelve todas las instancias de CarritoPorducto en Carrito
    def mostrar_carrito(self):
        return self.productos

    # calcula el precio total del conjunto de productos en el carrito
    def calcular_total(self):
        carritoproductos = self.mostrar_carrito()
        if len(list(carritoproductos)):
            total = sum(item.producto.precio * item.cantidad for item in carritoproductos)
            self.total = total
        else:
            self.total = 0.0
        self.save()
        return self.total