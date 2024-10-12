from __init__ import *

db = SqliteDatabase('database.db')

def getdatabase():
    return db
#como medida de seguridad creamos la variable db que contiene a la bd, a su vez definmos getdatabase que ba a retornar db que a su ves es la bd,
# desp, desde vamos a crear una clase "BaseModel"  donde le vamos a pasar por parametro database (base de datos) y le vamos a pasar al parametro getdatabase