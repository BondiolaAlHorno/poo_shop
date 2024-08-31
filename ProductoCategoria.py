from __init__ import *

class ProductoCategoria(BaseModel):
    producto = ForeignKeyField(Producto, backref='categoriasproducto')
    categoria = ForeignKeyField(Categoria, backref='productoscategoria')

    def getproducto(self):
        return self.producto
    def setproducto(self,new):
        self.producto = new
    
    def getcategoria(self):
        return self.categoria
    def setcategoria(self,new):
        self.categoria = new