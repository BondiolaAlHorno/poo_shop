from __init__ import *
import os

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

Administrador.alta_administrador(
                    'manolo',
                     'manolin',
                     '0303456',
                     '1234567',
                     'manolitomanolin@mail.dominio',
                     'manolito',
                     'contrasenia'
                    )

Cliente.alta_cliente('manuelita',
                     'pehuajo',
                     '0303456',
                     '1234567',
                     'pedrope@mail.dominio',
                     'mi casa',
                     'manuelita',
                     'contrasenia'
                     )

placa=Producto.create(descripcion='placa de video', precio=200000.0, stock=12, marca='nvidia', modelo='gtx 1660ti')
procesador=Producto.create(descripcion='procesador', precio=140000.0, stock=15, marca='intel', modelo='i5 12400f')
procesador2=Producto.create(descripcion='procesador', precio=360000.0, stock=15, marca='intel', modelo='i7 12700kf')

cpu=Categoria.create(nombre = 'cpu')
intel=Categoria.create(nombre = 'intel')
gpu=Categoria.create(nombre = 'gpu')
nvidia=Categoria.create(nombre = 'nvidia')

placa.agregar_categoria(gpu)
placa.agregar_categoria(nvidia)

procesador.agregar_categoria(cpu)
procesador.agregar_categoria(intel)

procesador2.agregar_categoria(cpu)
procesador2.agregar_categoria(intel)




print('TERMINADO')