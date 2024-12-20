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
    def alta_cliente(nombre:str, apellido:str, telefono:str, documento:str, mail:str, direccion:str, usuario:str, contrasenia:str):
        from Carrito import Carrito
        with getdatabase().atomic():

            user=Usuario.crearusuario(
                'cliente',
                usuario,
                contrasenia
                )
            
            cliente = Cliente.create(
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                documento=documento,
                mail=mail,
                direccion=direccion,
                usuario=user
                )
            
            Carrito.create(
                total=0,
                cliente=cliente
                )

    # retorna todos los datos del cliente
    def ver_datos_cuenta(self):
        return [self.iden, self.nombre, self.apellido, self.telefono, self.documento, self.mail, self.direccion, self.usuario.usuario]
    
    # conjuntod e funciones para modificar los datos del cliente
    def modificar_nombre(self,nombre:str):
        if self.nombre != nombre and nombre != '':
            self.setnombre(nombre)
            self.save()
            return True
        else:
            return False
    
    def modificar_apellido(self,apellido:str):
        if self.apellido != apellido and apellido != '':
            self.setapellido(apellido)
            self.save()
            return True
        else:
            return False
    
    def modificar_telefono(self,telefono:str):
        if self.telefono != telefono and telefono != '':
            self.settelefono(telefono)
            self.save()
            return True
        else:
            return False
    
    def modificar_documento(self,documento:str):
        if self.documento != documento and documento != '':
            self.setdocumento(documento)
            self.save()
            return True
        else:
            return False
    
    def modificar_mail(self,mail:str):
        if self.mail != mail and mail != '':
            self.setmail(mail)
            self.save()
            return True
        else:
            return False
    
    def modificar_direccion(self,direccion:str):
        if self.direccion != direccion and direccion != '':
            self.setdireccion(direccion)
            self.save()
            return True
        else:
            return False

    # @staticmethod
    # def enviar_mail_de_verificacion(mail:str):
    #     import smtplib
    #     from email.mime.text import MIMEText
    #     from email.mime.multipart import MIMEMultipart

    #     smtp_server = 'smtp.gmail.com'
    #     smtp_port = 587
    #     usuario = 'hugogilardoniestudia@gmail.com'
    #     contrasenia = 'Dibujeelpatron123@'

    #     de = 'hugogilardoniestudia@gmail.com'
    #     para = mail
    #     asunto = 'prueba de correo de confirmacion'
    #     cuerpo = 'este es el correo de confirmacion'

    #     msg = MIMEMultipart()
    #     msg['From'] = de
    #     msg['To'] = para
    #     msg['Subject'] = asunto

    #     msg.attach(MIMEText(cuerpo, 'plain'))

    #     try:
    #         server = smtplib.SMTP(smtp_server, smtp_port)
    #         server.starttls()
    #         server.login(usuario, contrasenia)
    #         server.send_message(msg)
    #         server.quit()
    #         return True
    #     except:
    #         server.quit()
    #         return False
