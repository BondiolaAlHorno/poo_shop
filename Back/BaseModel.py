from __init__ import *

class BaseModel(Model):
    class Meta:
        database = getdatabase()