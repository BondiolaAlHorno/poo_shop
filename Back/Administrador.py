from __init__ import *
#importamos "Init" que trae a este archivo todas las clases

class Administrador(Persona): #definimos la clase admnin
    pass #segui scroleando aca no hay nada

#pasamos a definir los metodos
    def altaAdmin(self, id,nom,ape,tel,dni,email,usuar): # le voy a pasar por parametros nuevos "atributos", correspondiente a cada atributo de la clae padre en este caso, ejemplo claro de como hereda lso atributos de persona el administrador
        return Administrador.create(iden=id,nombre=nom,apellido=ape,telefono=tel, documento=dni,mail=email, usuarios=usuar)
                
    def eliminarAdmin(self): # elimina lo que esta entre parentesis, en este caso self
        self.delete_instance()