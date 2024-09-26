from peewee import *

db = SqliteDatabase('database.db')

def getdatabase():
    return db

class BaseModel(Model):
    class Meta:
        database = getdatabase()

class Persona(BaseModel):
    iden = PrimaryKeyField()
    nombre = CharField()
    apellido = CharField()
    telefono = CharField(11)
    documento = CharField(7)
    mail = CharField()

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def getnombre(self):
        return self.nombre
    def setnombre(self, new):
        self.nombre = new

    def getapellido(self):
        return self.apellido
    def setapellido(self, new):
        self.apellido = new

    def gettelefono(self):
        return self.telefono
    def settelefono(self, new):
        self.telefono = new

    def getdocumento(self):
        return self.documento
    def setdocumento(self, new):
        self.documento = new

    def getmail(self):
        return self.mail
    def setmail(self, new):
        self.mail = new

class Usuario(BaseModel):
    iden = PrimaryKeyField()
    tipo = CharField()
    usuario = CharField()
    contrasenia = CharField()
    persona = ForeignKeyField(Persona, backref='usuarios')

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def gettipo(self):
        return self.tipo
    def settipo(self, new):
        self.tipo = new

    def getusuario(self):
        return self.usuario
    def setusuario(self, new):
        self.usuario = new

    def getcontrasenia(self):
        return self.contrasenia
    def setcontrasenia(self, new):
        self.contrasenia = new

    def getpersona(self):
        return self.persona
    def setpersona(self,new):
        self.persona = new

class Administrador(Persona):
    pass

class Cliente(Persona):
    direccion = CharField()

    def getdireccion(self):
        return self.direccion
    def setdireccion(self, new):
        self.direccion = new

class Carrito(BaseModel):
    iden = PrimaryKeyField()
    total = DecimalField()
    cliente = ForeignKeyField(Cliente, backref='carrito')

    def getiden(self):
        return self.iden
    def setiden(self,new):
        self.iden = new

    def gettotal(self):
        return self.total
    def settotal(self,new):
        self.total = new

    def getcliente(self):
        return self.cliente
    def setcliente(self,new):
        self.cliente = new

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

class Pago(BaseModel):
    iden = PrimaryKeyField()
    total = DecimalField()
    metododepago = CharField()
    numerodetarjeta = CharField()
    estado = CharField()

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def gettotal(self):
        return self.total
    def settotal(self, new):
        self.total = new

    def getmetododepago(self):
        return self.metododepago
    def setmetododepago(self, new):
        self.metododepago = new

    def getnumerodetarjeta(self):
        return self.numerodetarjeta
    def setnumerodetarjeta(self, new):
        self.numerodetarjeta = new

    def getestado(self):
        return self.estado
    def setestado(self, new):
        self.estado = new

class Producto(BaseModel):
    iden = PrimaryKeyField()
    descripcion = CharField(270)
    precio = DecimalField(10,2)
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
        ProductoCategoria.create(producto=self, categoria=categoria)

    def eliminar_categoria(self, categoria):
        try:
            relacion = ProductoCategoria.get(ProductoCategoria.producto == self, ProductoCategoria.categoria == categoria)
            relacion.delete_instance()
        except ProductoCategoria.DoesNotExist:
            raise ValueError("La categoría no está asociada a este producto.")
        
    def get_id_categorias(self):
        categorias = (ProductoCategoria.select(ProductoCategoria.categoria).where(ProductoCategoria.producto == self))
        return [cat.categoria.id for cat in categorias]
    
    def get_nombre_categorias(self):
        categorias = (ProductoCategoria.select(ProductoCategoria.categoria).where(ProductoCategoria.producto == self))
        return [cat.categoria.nombre for cat in categorias]
    
    def lista_productos_por_categoria(self,cat):
        productos = (ProductoCategoria.select(ProductoCategoria.producto).where(ProductoCategoria.categoria == cat))
        return [producto.producto for producto in productos]
    
    def obtener_datos_producto(self):
        return [self.iden, self.descripcion, self.precio, self.stock, self.marca, self.modelo]
    
    def añadir_producto(self):
        ProductoCategoria.create(producto=self)

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

class Venta(BaseModel):
    iden = PrimaryKeyField()
    estado = CharField()
    pago = ForeignKeyField(Pago, backref='venta')
    fecha = CharField()
    cliente = ForeignKeyField(Cliente, backref='historial')
    envio = DecimalField(10,2)
    total = DecimalField(10,2)

    def getiden(self):
        return self.iden
    def setiden(self, new):
        self.iden = new

    def getestado(self):
        return self.estado
    def setestado(self, new):
        self.estado = new

    def getpago(self):
        return self.pago
    def setpago(self, new):
        self.pago = new

    def getfecha(self):
        return self.fecha
    def setfecha(self, new):
        self.fecha = new

    def getcliente(self):
        return self.cliente
    def setcliente(self, new):
        self.cliente = new

    def getenvio(self):
        return self.envio
    def setenvio(self, new):
        self.envio = new

    def gettotal(self):
        return self.total
    def settotal(self, new):
        self.total = new

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

class CarritoProducto(BaseModel):
    carrito = ForeignKeyField(Carrito, backref='productos')
    producto = ForeignKeyField(Producto, backref='carritos')
    cantidad = IntegerField()

    def gatcarrito(self):
        return self.carrito
    def setcarrito(self,new):
        self.carrito = new

    def getproducto(self):
        return self.producto
    def setprodcuto(self,new):
        self.producto = new

    def getcantidad(self):
        return self.cantidad
    def setcantidad(self,new):
        self.cantidad = new

class VentaProducto(BaseModel):
    venta = ForeignKeyField(Venta, backref='productos')
    producto = ForeignKeyField(Producto, backref='ventas')
    cantidad = IntegerField()

    def getventa(self):
        return self.venta
    def setventa(self,new):
        self.venta = new

    def getproducto(self):
        return self.producto
    def setproducto(self,new):
        self.producto = new
    
    def getcantidad(self):
        return self.cantidad
    def setcantidad(self,new):
        self.cantidad = new

db = getdatabase()
db.connect()
def ceratetables():
    db.create_tables([Administrador,
                      Carrito,
                      CarritoProducto,
                      Categoria,
                      Cliente,
                      Pago,
                      Persona,
                      Producto,
                      ProductoCategoria,
                      Usuario,
                      Venta,
                      VentaProducto], safe = True)

ceratetables()

# Crear un producto
producto = Producto.create(descripcion="placa de video de gama baja", precio=100.00, stock=10, marca="nvidia", modelo="gtx 1660 ti")

# Crear categorías
categoria1 = Categoria.create(nombre="videocard")
categoria2 = Categoria.create(nombre="low-end")

# Agregar categorías al producto
producto.agregar_categoria(categoria1)
producto.agregar_categoria(categoria2)

# Obtener y mostrar las categorías del producto
nombres_categorias = producto.get_nombre_categorias()
print(f"Categorías del producto {producto.descripcion}: {nombres_categorias}")

# Eliminar una categoría
producto.eliminar_categoria(categoria1)

# Mostrar categorías después de la eliminación
nombres_categorias_actualizadas = producto.get_nombre_categorias()
print(f"Categorías del producto {producto.descripcion} después de eliminar: {nombres_categorias_actualizadas}")