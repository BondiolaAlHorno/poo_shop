from __init__ import *

class Usuario(BaseModel):
    iden = PrimaryKeyField()
    tipo = CharField()
    usuario = CharField()
    contrasenia = CharField()

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
    def crearusuario(tipo_usuario:str,usuario:str,contrasenia:str):
        return Usuario.create(
                tipo=tipo_usuario,
                usuario=usuario,
                contrasenia=contrasenia
            )

    # modifica el nombre del usuario, se le pasa el nuevo nombre de usuario y la contraseña, y si la contraseña es correcta modifica el nombre del usuario
    def modificarusuario(self,contrasenia:str,usuario:str):
        if self.contrasenia == contrasenia:
            self.setusuario(usuario)
            self.save()
            return True
        else:
            return False

    # modifica la contraseña del usuario, se le pasa la nueva contraseña de usuario y la antigua contraseña, y si la contraseña es correcta modifica la contraseña del usuario
    def modificarcontrasenia(self,vieja:str,nueva:str):
        if self.contrasenia == vieja:
            self.setcontrasenia(nueva)
            self.save()
            return True
        else:
            return False

    # verifica si un usuario existe, si es asi retorna true y un objeto usuario, sino retorna false, se le pasa un nombre de ususario
    @staticmethod
    def verificar_usuario(usua:str):
        try:
            pers= Usuario.get(Usuario.usuario==usua)
            return True,pers
        except Usuario.DoesNotExist:
            return False,False
    
    # verifica si la contraseña carresponde  aun usuario en particular, se le pasa una contraseña y un objeto usuario
    @staticmethod
    def verificar_contrasenia(contra:str,usua:'Usuario'):
        if usua.contrasenia == contra:
            return True
        else:
            return False
        
    # verifica si el usuario y la contraseña son correctos, si es asi retona true, sino false
    @staticmethod
    def verificar_usuario_contraseña(usua:str,contra:str):
        resultado, usuario = Usuario.verificar_usuario(usua)
        if resultado and Usuario.verificar_contrasenia(contra,usuario):
            return True
        else:
            return False
        
    # inicia la sesion de un usuario
    @staticmethod
    def iniciarsesion(usuario,contrasenia):
        import os
        from Cliente import Cliente
        from Administrador import Administrador
        while True:
            if usuario == '' and contrasenia == '':
                    return None
            if Usuario.verificar_usuario_contraseña(usuario,contrasenia):
                user = Usuario.get(Usuario.usuario == usuario, Usuario.contrasenia == contrasenia)
                if user.tipo == 'cliente':
                    pers = Cliente.get(Cliente.usuario == user)
                else:
                    pers = Administrador.get(Administrador.usuario == user)
                return pers
            else:
                os.system('cls')
                print('Usuario o Contraseña incorretos')
                usuario=input('Usuario:  ')
                contrasenia=input('Contraseña:  ')
                if usuario == '' and contrasenia == '':
                    return None