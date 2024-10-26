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


# Cliente.alta_cliente('hugo',
#                      'gilardoni',
#                      '0303456',
#                      '1234567',
#                      'hugogilardoni@estoesunmail.dominio',
#                      'mi casa',
#                      'bondiola',
#                      'contrasenia'
#                      )

# usu = Usuario.get(Usuario.usuario == 'bondiola')
# usu.delete_instance()

# pers = Cliente.get(Cliente.nombre == 'hugo')
# pers = Cliente.get()
# carri = pers.carrito.get()

# carri.anadir_producto_al_carrito(Producto.get(Producto.iden == 2), 1)
# carri.anadir_producto_al_carrito(Producto.get(Producto.iden == 3), 1)

# carri.modificar_carrito(Producto.get(Producto.iden == 2), 0)

# carri.confirmar_carrito('sin pagar','hoy', 10)

# venta = Venta.get()

# venta.realizar_pedido('visa','0303456')

# venta.estado = 'Confirmado'
# venta.save()
# print(venta.cancelar_pedido())

# print(venta.pago.get().estado)

# print(venta.mostrar_productos())

# print(carri.total)

# print(pers.vercarrito())

# print(pers.modificar_nombre('huguito'))

# pers.delete_instance()

# pers.modificarcontrasenia('contrasenia','1234')
# print(pers.verificar_usuario_contraseña('bondiola','1234'))



# Producto.añadir_producto('placa de video',
#                          200000,
#                          15,
#                          'nvidia',
#                          'gtx 1660 ti'
#                          )

# Producto.añadir_producto('procesador',
#                          150000,
#                          30,
#                          'intel',
#                          'i5 12400f'
#                          )

# Categoria.agregar_categoria('nvidia')
# categorias=Categoria.obtener_lista_categorias()
# categorias[1].eliminar_categoria()

# productos=list(Producto.select())
# productos[0].eliminar_categoria(categorias[1])
# print(productos[0].get_nombre_categorias())
# productosporcategoria=Producto.lista_productos_por_categoria(categorias[1])
# productosporcriterio=Producto.lista_productos_por_cariterio('placa')
# print([item.obtener_datos_producto() for item in productosporcriterio])

# productos[0].modificar_descripcion('placa de video nvidia')
# print(productos[0].obtener_datos_producto())

# productos[0].agregar_categoria(categorias[1])

# # Crear un producto
# producto = Producto.create(descripcion="placa de video de gama baja", precio=100.00, stock=10, marca="nvidia", modelo="gtx 1660 ti")

# # Crear categorías
# categoria1 = Categoria.create(nombre="videocard")
# categoria2 = Categoria.create(nombre="low-end")

# # Agregar categorías al producto
# producto.agregar_categoria(categoria1)
# producto.agregar_categoria(categoria2)

# # Obtener y mostrar las categorías del producto
# nombres_categorias = producto.get_nombre_categorias()
# print(f"Categorías del producto {producto.descripcion}: {nombres_categorias}")

# # Eliminar una categoría
# producto.eliminar_categoria(categoria1)

# # Mostrar categorías después de la eliminación
# nombres_categorias_actualizadas = producto.get_nombre_categorias()
# print(f"Categorías del producto {producto.descripcion} después de eliminar: {nombres_categorias_actualizadas}")