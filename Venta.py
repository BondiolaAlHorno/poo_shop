from __init__ import *

class Venta(BaseModel):
    iden = PrimaryKeyField()
    estado = CharField()
    pago = ForeignKeyField(Pago, backref='venta')
    fecha = CharField()
    cliente = ForeignKeyField(Cliente, backref='historial')
    envio = DecimalField()
    total = DecimalField()

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