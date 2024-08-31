from __init__ import *

db = getdatabase()

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
                      VentaProducto])

db.connect()
# ceratetables()