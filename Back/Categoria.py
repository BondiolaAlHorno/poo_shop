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
        
    def agregar_categoria(self):
        self.save()
        return self

    def eliminar_categoria(self):
        if self.iden:
            return self.delete_instance()
        return False

    def modificar_categoria(self, nuevo_nombre):
        if self.iden:
            self.nombre = nuevo_nombre
            self.save()
            return True
        return False

    @staticmethod
    def obtener_todas_las_categorias():
        return list(Categoria.select())
