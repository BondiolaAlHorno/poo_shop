from __init__ import *

class Categoria(BaseModel):
    iden = PrimaryKeyField()
    nombre = CharField()

    def getiden(self):
        return self.iden

    def getnombre(self):
        return self.nombre
    def setnombre(self, new):
        self.nombre = new
    
    # crea una, se le pasa el nombre de la misma
    @staticmethod
    def agregar_categoria(new:str):
        Categoria.create(nombre = new)

    # elimina la categoria
    def eliminar_categoria(self):
        self.delete_instance()

    # modifica el nombre de la categoria, se le pasa el nombre de la categoria
    def modificar_categoria(self, nuevo_nombre:str):
        self.setnombre(nuevo_nombre)
        self.save()

    # retorna una lista de categorias
    @staticmethod
    def obtener_lista_categorias():
        return list(Categoria.select())
