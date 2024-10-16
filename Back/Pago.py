from __init__ import *

class Pago(BaseModel):
    iden = PrimaryKeyField()
    total = DecimalField()
    metododepago = CharField()
    numerodetarjeta = CharField()
    estado = CharField()
    venta = ForeignKeyField(Venta, backref='pago')

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def gettotal(self):
        return self.total
    def settotal(self, new):
        self.total = new

    def getmetododepago(self):
        return self.metododepago
    def setmetododepago(self, new):
        self.metododepago = new

    def getnumerodetarjeta(self):
        return self.numerodetarjeta
    def setnumerodetarjeta(self, new):
        self.numerodetarjeta = new

    def getestado(self):
        return self.estado
    def setestado(self, new):
        self.estado = new

    def getventa(self):
        return self.venta
    def setventa(self, new):
        self.venta = new
        
    def realizar_pago(self):
        # aca tiene que ir la logica para procesar el pago?
        if self.validar_pago():
            self.estado = "Completado"
            self.save()
            return True
        else:
            self.estado = "Fallido"
            self.save()
            return False
        
    def validar_pago(self):
        # aca tendria que ir la lógica para validar el pago??
        # ejemplo, verificar fondos suficientes, tarjeta válida, etc.
        return True