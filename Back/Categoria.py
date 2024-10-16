from __init__ import *

class Categoria(BaseModel):
    iden = PrimaryKeyField()
    nombre = CharField()

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def getnombre(self):
        return self.nombre
    def setnombre(self, new):
        self.nombre = new
        
    @staticmethod
    def agregar_categoria(new):
        return Categoria.create(nombre = new)

    def eliminar_categoria(self):
        self.delete_instance()

    def modificar_categoria(self, nuevo_nombre):
        self.setnombre(nuevo_nombre)

    @staticmethod
    def obtener_lista_categorias():
        return list(Categoria.select())
