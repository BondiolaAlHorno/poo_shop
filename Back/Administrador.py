from __init__ import *
#importamos "Init" que trae a este archivo todas las clases

class Administrador(Persona):
    pass

    # crea un administrador junto con su usuario, recibe: nombre, apellido, telefono, documento, mail, direccion, tipo_usuario, usuario, contraseña
    @staticmethod
    def alta_administrador(nombre, apellido, telefono, documento, mail, direccion, tipo_usuario, usuario, contrasenia):
        with getdatabase().atomic():
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
    
    # elimina un administrador
    def eliminarAdmin(self):
        self.delete_instance()