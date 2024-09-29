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
        
    @classmethod
    def agregar_categoria(cls, nombre):
        return cls.create(nombre=nombre)

    @classmethod
    def eliminar_categoria(cls, iden):
        categoria = cls.get_or_none(cls.iden == iden)
        if categoria:
            categoria.delete_instance()
            return True
        return False

    @classmethod
    def modificar_categoria(cls, iden, nuevo_nombre):
        categoria = cls.get_or_none(cls.iden == iden)
        if categoria:
            categoria.nombre = nuevo_nombre
            categoria.save()
            return True
        return False

    @classmethod
    def obtener_todas_las_categorias(cls):
        return list(cls.select())
        
    # No se si esto esta bien, huguito confirmalo