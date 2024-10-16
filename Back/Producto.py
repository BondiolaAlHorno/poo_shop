from __init__ import *

class Producto(BaseModel):
    iden = PrimaryKeyField()
    descripcion = CharField()
    precio = DecimalField()
    stock = IntegerField()
    marca = CharField()
    modelo = CharField()

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def getdescripcion(self):
        return self.descripcion
    def setdescripcion(self, new):
        self.descripcion = new

    def getprecio(self):
        return self.precio
    def setprecio(self, new):
        self.precio = new

    def getstock(self):
        return self.stock
    def setstock(self, new):
        self.stock = new

    def getmarca(self):
        return self.marca
    def setmarca(self, new):
        self.marca = new

    def getmodelo(self):
        return self.modelo
    def setmodelo(self, new):
        self.modelo = new

    def agregar_categoria(self, categoria):
        from ProductoCategoria import ProductoCategoria
        ProductoCategoria.create(producto=self, categoria=categoria)

    def eliminar_categoria(self, categoria):
        from ProductoCategoria import ProductoCategoria
        try:
            relacion = ProductoCategoria.get(ProductoCategoria.producto == self, ProductoCategoria.categoria == categoria)
            relacion.delete_instance()
        except ProductoCategoria.DoesNotExist:
            raise ValueError("La categoría no está asociada a este producto.")
        
    def get_id_categorias(self):
        from ProductoCategoria import ProductoCategoria
        categorias = (ProductoCategoria.select(ProductoCategoria.categoria).where(ProductoCategoria.producto == self))
        return [cat.categoria.id for cat in categorias]
    
    def get_nombre_categorias(self):
        from ProductoCategoria import ProductoCategoria
        categorias = (ProductoCategoria.select(ProductoCategoria.categoria).where(ProductoCategoria.producto == self))
        return [cat.categoria.nombre for cat in categorias]
    
    def lista_productos_por_categoria(self,cat):
        from ProductoCategoria import ProductoCategoria
        productos = (ProductoCategoria.select(ProductoCategoria.producto).where(ProductoCategoria.categoria == cat))
        return [producto.producto for producto in productos]
    
    def obtener_datos_producto(self):
        return [self.iden, self.descripcion, self.precio, self.stock, self.marca, self.modelo]
    
    @staticmethod
    def añadir_producto(descripcion = None, precio = None, stock = None, marca = None, modelo = None):
        Producto.create(descripcion=descripcion, precio=precio, stock=stock, marca=marca, modelo=modelo)

    def eliminar_producto(self):
        self.delete_instance()

    def modificar_producto(self, descripcion = None, precio = None, stock = None, marca = None, modelo = None):
        if (descripcion != None) and (descripcion != self.descripcion):
            self.descripcion = descripcion
        if (precio != None) and (precio != self.precio):
            self.precio = precio
        if (stock != None) and (stock != self.stock):
            self.stock = stock
        if (marca != None) and (marca != self.marca):
            self.marca = marca
        if (modelo != None) and (modelo != self.modelo):
            self.modelo = modelo