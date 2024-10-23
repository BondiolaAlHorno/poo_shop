from __init__ import *

# se instancia la base de datos
db = SqliteDatabase('database.db')

# retorna la base de datos
def getdatabase():
    return db
