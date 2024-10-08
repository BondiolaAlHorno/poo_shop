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
        
    def agregar_categoria(self,new):
        return Categoria.create(nombre = new)

    def eliminar_categoria(self):
        if self.iden:
            return self.delete_instance()
        return False

    def modificar_categoria(self, nuevo_nombre):
        self.setnombre(nuevo_nombre)

    @staticmethod
    def obtener_todas_las_categorias():
        return list(Categoria.select())
