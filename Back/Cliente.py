from __init__ import *

class Cliente(Persona):
    direccion = CharField()

    def getdireccion(self):
        return self.direccion
    def setdireccion(self, new):
        self.direccion = new

    def gethistorial(self):
        return self.carrito
    
    def altaCliente(self,id,nom,ape,tel,dni,email, usuar,dire):
        return Cliente.create(iden=id,nombre=nom,apellido=ape,telefono=tel, documento=dni,mail=email, usuarios= usuar, direccion= dire)
    # def inicioSesion() es un bardo

    # def cerrarSesion() es otro bardo

    def verDatosCuenta(self):
        return [self.iden, self.nombre, self.apellido, self.telefono, self.documento, self.mail, self.usuarios, self.direccion]

    def modificarDatosCiente(self,id):
        if self.iden != id:
            self.setiden(id)
            