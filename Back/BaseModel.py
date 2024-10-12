from __init__ import *
#se crea una clase padre BaseModel, y se pasa por parametro MODEL que tiene muuuucho codigo
class BaseModel(Model): 
    class Meta:  #se crea la clase Meta
        database = getdatabase() # creamos el atributo database, con el fin de que me traigha el get data base que es el llamado a la bd q te proporciona peewee