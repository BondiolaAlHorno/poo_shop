from __init__ import *

class Venta(BaseModel):
    iden = PrimaryKeyField()
    estado = CharField()
    fecha = CharField()
    envio = DecimalField()
    total = DecimalField()
    cliente = ForeignKeyField(Cliente, backref='historial')

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def getestado(self):
        return self.estado
    def setestado(self, new):
        self.estado = new

    def getpago(self):
        return self.pago
    def setpago(self, new):
        self.pago = new

    def getfecha(self):
        return self.fecha
    def setfecha(self, new):
        self.fecha = new

    def getenvio(self):
        return self.envio
    def setenvio(self, new):
        self.envio = new

    def gettotal(self):
        return self.total
    def settotal(self, new):
        self.total = new

    def getcliente(self):
        return self.cliente
    def setcliente(self, new):
        self.cliente = new

    def get_metodo_pago_pago(self):
        return self.pago.getmetododepago()
    
    def get_numero_tarjeta_pago(self):
        return self.pago.getnumerodetarjeta()
    
    def get_estado_pago(self):
        return self.pago.getestado()
    
    def get_precio_producto(self,producto):
        return producto.precio
        
    def get_nombre_cliente(self):
        return self.cliente.getnombre()

    def get_apellido_cliente(self):
        return self.cliente.getapellido()

    def get_documento_cliente(self):
        return self.cliente.getdocumento()

    def mostrar_productos(self):
        return self.productos

    def calcular_total(self):
        total = sum(item.producto.precio * item.cantidad for item in self.mostrar_productos())
        self.total = total
        self.save()
        return self.total

    def calcular_envio(self):
        # Aca tiene que ir la lógica para calcular el costo de envío?
        self.envio = 10.0
        self.save()
        return self.envio

    def realizar_pedido(self):
        self.validar_stock()
        self.estado = "Confirmado"
        self.pago.realizar_pago()
        self.save()

    def cancelar_pedido(self):
        if self.estado != "Enviado":
            self.estado = "Cancelado"
            self.pago.setestado("Reembolsado")
            self.save()
            return True
        return False

    def validar_stock(self):
        for item in self.mostrar_productos:
            if item.producto.stock < item.cantidad & item.producto.stock > 0:
                item.cantidad = item.producto.stock
            elif item.producto.stock == 0:
                item.delete_instance()