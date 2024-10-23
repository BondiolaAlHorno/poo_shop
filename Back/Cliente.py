from __init__ import *

class Cliente(Persona):
    direccion = CharField()

    def getdireccion(self):
        return self.direccion
    def setdireccion(self, new):
        self.direccion = new

    def gethistorial(self):
        return self.historial
    
    # crea un cliente junto con su usuario, se le pasa como parametro: nombre, apellido, telefono, documento, mail, direccion, tipo_usuario, usuario, contrasenia
    @staticmethod
    def alta_cliente(nombre, apellido, telefono, documento, mail, direccion, tipo_usuario, usuario, contrasenia):
        with getdatabase().atomic():
            cliente = Cliente.create(
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
                cliente
                )

    # ewtorna todos los datos del cliente
    def verDatosCuenta(self):
        return [self.iden, self.nombre, self.apellido, self.telefono, self.documento, self.mail, self.direccion, self.usuarios.usuario, self.usuarios.contrasenia]
    
    # conjuntod e funciones para modificar los datos del cliente
    def modificar_nombre(self,nombre):
        if self.nombre != nombre and nombre != '':
            self.setnombre(nombre)
    
    def modificar_apellido(self,apellido):
        if self.apellido != apellido and apellido != '':
            self.setapellido(apellido)
    
    def modificar_telefono(self,telefono):
        if self.telefono != telefono and telefono != '':
            self.settelefono(telefono)
    
    def modificar_documento(self,documento):
        if self.documento != documento and documento != '':
            self.setdocumento(documento)
    
    def modificar_mail(self,mail):
        if self.mail != mail and mail != '':
            self.setmail(mail)
    
    def modificar_direccion(self,direccion):
        if self.direccion != direccion and direccion != '':
            self.setdireccion(direccion)

    # retorna una lista de tuplas del carrito donde cada una contiene un producto y su cantidad
    def vercarrito(self):
        return [(item.producto, item.cantidad) for item in self.carrito.mostrar_carrito()]