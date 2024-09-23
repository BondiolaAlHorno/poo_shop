from __init__ import *

class Venta(BaseModel):
    iden = PrimaryKeyField()
    estado = CharField()
    pago = ForeignKeyField(Pago, backref='venta')
    fecha = CharField()
    cliente = ForeignKeyField(Cliente, backref='historial')
    envio = DecimalField(10,2)
    total = DecimalField(10,2)

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

    def getcliente(self):
        return self.cliente
    def setcliente(self, new):
        self.cliente = new

    def getenvio(self):
        return self.envio
    def setenvio(self, new):
        self.envio = new

    def gettotal(self):
        return self.total
    def settotal(self, new):
        self.total = new
        
    def calcular_total(self):
        subtotal = sum(item.producto.precio * item.cantidad for item in self.items)
        self.total = subtotal + self.envio
        self.save()
        return self.total

    def calcular_envio(self):
        # Aca tiene que ir la lógica para calcular el costo de envío?
        self.envio = 10.0
        self.save()
        return self.envio

    def realizar_pedido(self):
        if self.validar_stock():
            self.estado = "Confirmado"
            self.pago.realizar_pago()
            self.save()
            return True
        return False

    def cancelar_pedido(self):
        if self.estado != "Enviado":
            self.estado = "Cancelado"
            self.pago.setestado("Reembolsado")
            self.save()
            return True
        return False

    def get_nombre_cliente(self):
        return self.cliente.getnombre()

    def get_apellido_cliente(self):
        return self.cliente.getapellido()

    def get_documento_cliente(self):
        return self.cliente.getdocumento()

    def validar_stock(self):
        for item in self.items:
            if item.producto.stock < item.cantidad:
                return False
        return True    