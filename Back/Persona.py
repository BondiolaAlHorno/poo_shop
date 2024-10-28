from __init__ import *

class Persona(BaseModel):
    iden = PrimaryKeyField()
    nombre = CharField()
    apellido = CharField()
    telefono = CharField()
    documento = CharField()
    mail = CharField()
    usuario = ForeignKeyField(Usuario, backref='persona',unique=True)

    def getiden(self):
        return self.iden

    def getnombre(self):
        return self.nombre
    def setnombre(self, new):
        self.nombre = new

    def getapellido(self):
        return self.apellido
    def setapellido(self, new):
        self.apellido = new

    def gettelefono(self):
        return self.telefono
    def settelefono(self, new):
        self.telefono = new

    def getdocumento(self):
        return self.documento
    def setdocumento(self, new):
        self.documento = new

    def getmail(self):
        return self.mail
    def setmail(self, new):
        self.mail = new
        
    def gettipo(self):
        return self.usuario.tipo
    
    def getusuario(self):
        return self.usuario
    
    def setusuaios(self,new):
        self.usuario=new
    
    def settipo(self,nuevotipo):
        self.usuario.tipo = nuevotipo
    
    def setusuario(self,new):
        self.usuario = new

    def getusuariousuario(self):
        return self.usuario.usuario
      
    def getcontraseniausuario(self):
        return self.usuario.contrasenia
    
    