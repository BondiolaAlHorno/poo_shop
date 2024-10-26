from __init__ import *
#importamos "Init" que trae a este archivo todas las clases

class Administrador(Persona):
    pass

    # crea un administrador junto con su usuario, recibe: nombre, apellido, telefono, documento, mail, direccion, tipo_usuario, usuario, contraseña
    @staticmethod
    def alta_administrador(nombre:str, apellido:str, telefono:str, documento:str, mail:str, usuario:str, contrasenia:str):
        with getdatabase().atomic():
            administrador = Administrador.create(
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                documento=documento,
                mail=mail,
            )
            
            Usuario.crearusuario(
                'administrador',
                usuario,
                contrasenia,
                administrador
                )
    
    # elimina un administrador
    def eliminar_administrador(self):
        self.delete_instance()