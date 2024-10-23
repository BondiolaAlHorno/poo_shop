from __init__ import *

class Usuario(BaseModel):
    iden = PrimaryKeyField()
    tipo = CharField()
    usuario = CharField()
    contrasenia = CharField()
    persona = ForeignKeyField(Persona, backref='usuarios')

    def getiden(self):
        return self.iden

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

    # crea un usuario
    @staticmethod
    def crearusuario(tipo_usuario,usuario,contrasenia,persona):
        Usuario.create(
                tipo=tipo_usuario,
                usuario=usuario,
                contrasenia=contrasenia,
                persona=persona
            )

    # modifica el nombre del usuario, se le pasa el nuevo nombre de usuario y la contraseña, y si la contraseña es correcta modifica el nombre del usuario
    def modificarusuario(self,contrasenia,usuario):     #FALTA DOCUMENTACION
        if self.contrasenia == contrasenia:
            self.setusuario(usuario)
        else:
            return False

    # modifica la contraseña del usuario, se le pasa la nueva contraseña de usuario y la antigua contraseña, y si la contraseña es correcta modifica la contraseña del usuario
    def modificarcontrasenia(self,vieja,nueva):     #FALTA DOCUMENTACION
        if self.contrasenia == vieja:
            self.setcontrasenia(nueva)
        else:
            return False

    # verifica si un usuario existe, si es asi retorna true y un objeto usuario, sino retorna false, se le pasa un nombre de ususario
    @staticmethod
    def veriUsuario(usua):
        try:
            pers= Usuario.get(Usuario.usuario==usua)
            return True,pers
        except Usuario.DoesNotExist:
            return False,False
    
    # verifica si la contraseña carresponde  aun usuario en particular, se le pasa una contraseña y un objeto usuario
    @staticmethod
    def veriContra(contra,usua:Usuario):
        if usua.contrasenia == contra:
            return True
        else:
            return False
        
    # verifica si el usuario y la contraseña son correctos, si es asi retona true, sino false
    @staticmethod
    def verificar_usuario_contraseña(usua,contra):
        resultado, usuario = Usuario.veriUsuario(usua)
        if resultado and Usuario.veriContra(contra,usuario):
            return True
        else:
            return False