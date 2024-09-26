from __init__ import *

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

# # Obtener y mostrar las categorías del producto
# nombres_categorias = producto.get_nombre_categorias()
# print(f"Categorías del producto {producto.descripcion}: {nombres_categorias}")

# # Eliminar una categoría
# producto.eliminar_categoria(categoria1)

# # Mostrar categorías después de la eliminación
# nombres_categorias_actualizadas = producto.get_nombre_categorias()
# print(f"Categorías del producto {producto.descripcion} después de eliminar: {nombres_categorias_actualizadas}")