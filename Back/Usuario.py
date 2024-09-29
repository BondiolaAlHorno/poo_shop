from __init__ import *

class Usuario(BaseModel):
    iden = PrimaryKeyField()
    tipo = CharField()
    usuario = CharField()
    contrasenia = CharField()
    persona = ForeignKeyField(Persona, backref='usuarios')

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new
    def gettipo(self):
        return self.tipo
    def settipo(self, new):
        self.tipo = new
    def getusuario(self):
        return self.usuario    
    def setusuario(self, new):
        self.usuario = new
    def getcontrasenia(self):
        return self.contrasenia    
    def setcontrasenia(self, new):
        self.contrasenia = new
    def veriUsuario(usua): #aca no se puede usar un if, porq da error, ¿pero en otras libriras se puede usar un if?? con un else
        try:
            pers= Usuario.get(Usuario.usuario==usua)
            return True
        except Usuario.DoesNotExist:
            return False
    def veriContra(contra):
        try:
            key= Usuario.get(Usuario.contrasenia==contra)
            return True
        except Usuario.DoesNotExist:
            return False