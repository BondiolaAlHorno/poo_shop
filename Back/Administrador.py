from __init__ import *
#importamos "Init" que trae a este archivo todas las clases

class Administrador(Persona): #definimos la clase admnin
    pass #segui scroleando aca no hay nada

#pasamos a definir los metodos
    @staticmethod
    def alta_administrador(nombre, apellido, telefono, documento, mail, direccion, tipo_usuario, usuario, contrasenia):
        from Constructor import db
        with db.atomic():
            administrador = Administrador.create(
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                documento=documento,
                mail=mail,
                direccion=direccion
            )
            
            Usuario.crearusuario(
                tipo_usuario,
                usuario,
                contrasenia,
                administrador
                )
                
    def eliminarAdmin(self): # elimina lo que esta entre parentesis, en este caso self
        self.delete_instance()