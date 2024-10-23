from __init__ import *
# clase base para modelos de la base de datos, que establece la conexión a la base de datos
# mediante la función getdatabase() para reducir la duplicación de código en los modelos
class BaseModel(Model): 
    class Meta:
        database = getdatabase()