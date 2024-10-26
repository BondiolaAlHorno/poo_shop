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

    # retorna una lista de id's de las categorias relacionadas con el producto
    def get_id_categorias(self):
        from ProductoCategoria import ProductoCategoria
        categorias = (ProductoCategoria.select(ProductoCategoria.categoria).where(ProductoCategoria.producto == self))
        return [cat.categoria.iden for cat in categorias]

    # retorna una lista de nombres de las categorias relacionadas con el producto
    def get_nombre_categorias(self):
        from ProductoCategoria import ProductoCategoria
        categorias = (ProductoCategoria.select(ProductoCategoria.categoria).where(ProductoCategoria.producto == self))
        return [cat.categoria.nombre for cat in categorias]
    
    # crea una relacion entre un producto y una categoria
    def agregar_categoria(self, categoria:Categoria):
        from ProductoCategoria import ProductoCategoria
        ProductoCategoria.create(producto=self, categoria=categoria)

    # elimina una relacion entre un producto y una categoria
    def eliminar_categoria(self, categoria:Categoria):
        from ProductoCategoria import ProductoCategoria
        try:
            relacion = ProductoCategoria.get(ProductoCategoria.producto == self, ProductoCategoria.categoria == categoria)
            relacion.delete_instance()
        except ProductoCategoria.DoesNotExist:
            raise ValueError("La categoría no está asociada a este producto.")
        
    # retorna una lista de productos que contengan una categoria en aprticular
    @staticmethod
    def lista_productos_por_categoria(cat):
        from ProductoCategoria import ProductoCategoria
        productos = (ProductoCategoria.select(ProductoCategoria.producto).where(ProductoCategoria.categoria == cat))
        return [producto.producto for producto in productos]
    
    @staticmethod
    def lista_productos_por_cariterio(criterio):
        from ProductoCategoria import ProductoCategoria
        productos = (Producto.select().where(Producto.descripcion.contains(criterio)))
        return list(productos)
    
    # retorna los datos del producto
    def obtener_datos_producto(self):
        return [self.iden, self.descripcion, self.precio, self.stock, self.marca, self.modelo]
    
    # crea un nuevo producto
    @staticmethod
    def añadir_producto(descripcion = None, precio = None, stock = None, marca = None, modelo = None):
        Producto.create(descripcion=descripcion, precio=precio, stock=stock, marca=marca, modelo=modelo)

    # elimina el producto
    def eliminar_producto(self):
        self.delete_instance()

    # conjuntod e funciones para modificar los datos del producto
    def modificar_descripcion(self, descripcion):
        if self.descripcion != descripcion and descripcion != '':
            self.setdescripcion(descripcion)
            self.save()
            return True
        else:
            return False

    def modificar_precio(self, precio):
        if self.precio != precio and precio is not None:
            self.setprecio(precio)
            self.save()
            return True
        else:
            return False

    def modificar_stock(self, stock):
        if self.stock != stock and stock is not None:
            self.setstock(stock)
            self.save()
            return True
        else:
            return False

    def modificar_marca(self, marca):
        if self.marca != marca and marca != '':
            self.setmarca(marca)
            self.save()
            return True
        else:
            return False

    def modificar_modelo(self, modelo):
        if self.modelo != modelo and modelo != '':
            self.setmodelo(modelo)
            self.save()
            return True
        else:
            return False