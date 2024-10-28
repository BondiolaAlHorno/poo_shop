from __init__ import *
import os
from datetime import datetime

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

while True:
    os.system('cls')
    
    entrada = input(
        '1. Iniciar sesion\n'
        '2. Crear Cliente\n'
        '3. Crear Administrador\n'
        'ENTER. Salir\n'
        )

    if entrada == '1':
        os.system('cls')
        pers = Usuario.iniciarsesion(input('Usuario:  '),input('Contraseña:  '))

        if pers!=None and pers.usuario.tipo == 'cliente':
            while True:
                os.system('cls')
                print(
                '1. Modificar datos de la cuenta\n'
                '2. Ver datos de la cuenta\n'
                '3. Carrito\n'
                '4. Productos\n'
                '5. Compra\n'
                'ENTER. Cerrar Sesion'
                )
                entrada2=input()

                if entrada2 == '1':
                    while True:
                        os.system('cls')
                        print(
                            '1. Modificar Nombre\n'
                            '2. Modificar Apellido\n'
                            '3. Modificar Telefono\n'
                            '4. Modificar Documento\n'
                            '5. Modificar Mail\n'
                            '6. Modificar Direccion\n'
                            '7. Modificar Usuario\n'
                            '8. Modificar Contraseña\n'
                            'ENTER. Salir\n'
                        )

                        modificar = input()

                        if modificar == '1':
                            os.system('cls')
                            nombre=input('Ingrese el nuevo Nombre:  ')
                            if nombre!='':
                                pers.modificar_nombre(nombre)
                        elif modificar == '2':
                            os.system('cls')
                            apellido=input('Ingrese el nuevo Apellido:  ')
                            if apellido!='':
                                pers.modificar_apellido(apellido)
                        elif modificar == '3':
                            os.system('cls')
                            telefono=input('Ingrese el nuevo Telefono:  ')
                            if telefono!='':
                                pers.modificar_telefono(telefono)
                        elif modificar == '4':
                            os.system('cls')
                            documento=input('Ingrese el nuevo Documento:  ')
                            if documento!='':
                                pers.modificar_documento(documento)
                        elif modificar == '5':
                            os.system('cls')
                            mail=input('Ingrese el nuevo Mail:  ')
                            if mail!='':
                                pers.modificar_mail(mail)
                        elif modificar == '6':
                            os.system('cls')
                            direccion=input('Ingrese la nueva Direccion:  ')
                            if direccion!='':
                                pers.modificar_direccion(direccion)
                        elif modificar == '7':
                            os.system('cls')
                            contrsenia=input('Ingrese su Contraseña:  ')
                            usuario=input('Ingrese el nuevo nombre de Usuario:  ')
                            if contrsenia!='' and usuario!='':
                                conf=pers.usuario.modificarusuario(contrsenia,usuario)
                                if not conf:
                                    input('Contraseña incorrecta')
                        elif modificar == '8':
                            os.system('cls')
                            contraseniavieja=input('Ingrese su Contraseña:  ')
                            contrasenianueva=input('Ingrese su nueva Contraseña:  ')
                            if contraseniavieja!='' and contrasenianueva!='':
                                conf=pers.usuario.modificarcontrasenia(contraseniavieja,contrasenianueva)
                                if not conf:
                                    input('Contraseña incorrecta')
                        elif modificar == '':
                            break
                        else:os.system('cls')

                elif entrada2 == '2':
                    os.system('cls')
                    indice = ['ID:  ','Nombre:  ','Apellido:  ','Telefono:  ','Documento:  ','Mail:  ','Direccion:  ','Usuario:  ']
                    for palabra,item in zip(indice,pers.ver_datos_cuenta()):
                        print(f'{palabra}{item}')
                    input()

                elif entrada2 == '3':
                    while True:
                        os.system('cls')
                        total=pers.carrito.get().calcular_total()
                        selectcarrito=input(
                            f'TOTAL: {total}\n'
                            '1. Ver y Modificar el Carrito\n'
                            '2. Confirmar el Carrito\n'
                            'ENTER. Salir\n'
                        )
                        if selectcarrito=='1':
                            while True:
                                os.system('cls')
                                carritoitems = pers.vercarrito()
                                for posicion,item in zip(range(len(carritoitems)),carritoitems):
                                    print(f'{posicion}  Modelo: {item[0]}  Cantidad: {item[1]}  Precio/u{item[2]}')
                                elemento=input('Seleccione un elemento para modificar su cantidad\n')
                                if elemento=='':
                                    break
                                else:
                                    pers.carrito.get().modificar_carrito(pers.carrito.get().mostrar_carrito()[int(elemento)].producto,int(input('Indique la nueva cantidad\n')))
                        if selectcarrito=='2':
                            if len(pers.carrito.get().mostrar_carrito())>0:
                                carritoventa=pers.carrito.get().confirmar_carrito(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),6700.0)
                                os.system('cls')
                                input('Carrito confirmado')
                            else:
                                os.system('cls')
                                input('No hay productos en el carrito')
                        if selectcarrito=='':
                            break

                elif entrada2 == '4':
                    while True:
                        os.system('cls')
                        print(
                            '1. Buscar por categoria\n'
                            '2. Buscar por criterio\n'
                            'ENTER. Salir'
                        )

                        inputproducto=input()

                        if inputproducto == '1':
                            os.system('cls')
                            liscat=Categoria.obtener_lista_categorias()
                            for item,posicion in zip(liscat,range(len(liscat))):
                                print(f'{posicion}  {item.nombre}')
                            cat=input('Seleccione una Categoria\n')
                            if cat=='':
                                pass
                            else:
                                while True:
                                    os.system('cls')
                                    productos = Producto.lista_productos_por_categoria(liscat[int(cat)])
                                    for item,posicion in zip(productos,range(len(productos))):
                                        print(f'{posicion}   Modelo: {item.modelo}   Stock: {item.stock}')
                                    print('Seleccione un item para agregarlo al carrito')
                                    agregar=input()
                                    if agregar=='':
                                        break
                                    else:
                                        cantidad=input('Seleccione la cantidad:\n')
                                        pers.carrito.get().anadir_producto_al_carrito(productos[int(agregar)],int(cantidad))

                        elif inputproducto == '2':
                            os.system('cls')
                            buscar=input('Buscar\n')
                            if buscar=='':
                                pass
                            else:
                                while True:
                                    os.system('cls')
                                    productos = Producto.lista_productos_por_cariterio(buscar)
                                    for item,posicion in zip(productos,range(len(productos))):
                                        print(f'{posicion}   Modelo: {item.modelo}   Stock: {item.stock}')
                                    print('Seleccione un item para agregarlo al carrito')
                                    agregar=input()
                                    if agregar=='':
                                        break
                                    else:
                                        cantidad=input('Seleccione la cantidad:\n')
                                        pers.carrito.get().anadir_producto_al_carrito(productos[int(agregar)],int(cantidad))

                        elif inputproducto == '':
                            break
                        else:os.system('cls')

                elif entrada2 == '5':
                    try:
                        carritoventa=Venta.get(Venta.iden == pers)
                        while True:
                            os.system('cls')
                            print(
                                f'Estado:  {carritoventa.getestado()}\n'
                                '1. Ver Productos'
                                )
                            if carritoventa.estado!='Cancelado' and carritoventa.estado!='Enviado' and carritoventa.estado!='Confirmado':
                                print('2. Realizar Pedido')
                            if carritoventa.pago and carritoventa.estado!='Cancelado' and carritoventa.estado!='Enviado':
                                print('3. Cancelar Pedido')
                            entradaventa=input()
                            if entradaventa == '1':
                                os.system('cls')
                                listaprodutosventa=carritoventa.mostrar_productos()
                                for item in listaprodutosventa:
                                    print(item)
                                input()
                            if entradaventa == '2' and carritoventa.estado!='Cancelado' and carritoventa.estado!='Enviado' and carritoventa.estado!='Confirmado':
                                os.system('cls')
                                carritoventa.realizar_pedido(input('Tipo de Tarjeta:  '),input('Numero de Tarjeta:  '))
                            if entradaventa == '3' and carritoventa.estado!='Cancelado' and carritoventa.estado!='Enviado':
                                os.system('cls')
                                carritoventa.cancelar_pedido()
                                input('Pedido Cancelado\n')
                            if entradaventa == '':
                                break
                    except:
                        os.system('cls')
                        input('No se a confirmado ningun carrito')


                elif entrada2 == '':
                    break

                else:
                    os.system('cls')

        elif pers!=None and pers.usuario.get().tipo == 'administrador':
            while True:
                os.system('cls')
                adminentrada=input(
                    '1. Productos\n'
                    '2. Categorias\n'
                    'ENTER. Cerrar Sesion\n'
                )

                if adminentrada == '1':
                    while True:
                        os.system('cls')
                        adminentrada2=input(
                            '1. Lista de Productos\n'
                            '2. Lista de Productos por Categoria\n'
                            '3. Lista de Productos por Criterio\n'
                            'ENTER. Salir\n'
                        )

                        if adminentrada2 == '1':
                            while True:
                                os.system('cls')
                                productos=Producto.lista_de_productos()
                                for item in productos:
                                    datos=item.obtener_datos_producto()
                                    print(f'ID: {item.iden},  Descripcion: {item.descripcion},  Precio: {item.precio},  Stock: {item.stock},  Marca: {item.marca},  Modelo: {item.modelo}')
                                selectproductos=input('Seleccione la ID de un Producto para modificarlo\n')
                                if selectproductos!='':
                                    while True:
                                        os.system('cls')
                                        modificarproducto=Producto.get(Producto.iden == selectproductos)
                                        print(f'ID: {modificarproducto.iden},  Descripcion: {modificarproducto.descripcion},  Precio: {modificarproducto.precio},  Stock: {modificarproducto.stock},  Marca: {modificarproducto.marca},  Modelo: {modificarproducto.modelo}')
                                        modificar=input(
                                            '1. Modificar Descripcion\n'
                                            '2. Modificar Precio \n'
                                            '3. Modificar Stock\n'
                                            '4. Modificar Marca\n'
                                            '5. Modificar Modelo\n'
                                            '6. Añadir Categoria\n'
                                            '7. Eliminar Categoria\n'
                                            '8. Eliminar Producto \n'
                                            'ENTER. Salir \n'
                                        )
                                        if modificar == '1':
                                            os.system('cls')
                                            modificarproducto.modificar_descripcion(input('Descripcion: \n'))
                                        elif modificar == '2':
                                            os.system('cls')
                                            modificarproducto.modificar_precio(float(input('Precio: \n')))
                                        elif modificar == '3':
                                            os.system('cls')
                                            modificarproducto.modificar_stock(int(input('Stock: \n')))
                                        elif modificar == '4':
                                            os.system('cls')
                                            modificarproducto.modificar_marca(input('Marca: \n'))
                                        elif modificar == '5':
                                            os.system('cls')
                                            modificarproducto.modificar_modelo(input('Modelo: \n'))
                                        elif modificar == '6':
                                            while True:
                                                os.system('cls')
                                                liscat=Categoria.obtener_lista_categorias()
                                                liscatproducto=modificarproducto.get_categorias()
                                                liscatfiltrada=[categoria for categoria in liscat if categoria not in liscatproducto]
                                                for item in liscatfiltrada:
                                                    print(f'ID: {item.iden}  Nombre: {item.nombre}')
                                                cat=input('Seleccione una Categoria\n')
                                                if cat=='':
                                                    break
                                                else:
                                                    modificarproducto.agregar_categoria(Categoria.get(Categoria.iden==cat))
                                        elif modificar == '7':
                                            while True:
                                                os.system('cls')
                                                listcat=modificarproducto.get_categorias()
                                                for item in listcat:
                                                    print(f'ID: {item.iden}  Nombre: {item.nombre}')
                                                cat=input('Seleccione una Categoria\n')
                                                if cat=='':
                                                    break
                                                else:
                                                    modificarproducto.eliminar_categoria(Categoria.get(Categoria.iden==cat))

                                        elif modificar == '8':
                                            os.system('cls')
                                            modificarproducto.eliminar_producto()
                                        elif modificar == '':
                                            os.system('cls')
                                            break
                                    
                                else:
                                    break
                        if adminentrada2 == '2':
                            os.system('cls')
                            liscat=Categoria.obtener_lista_categorias()
                            for item,posicion in zip(liscat,range(len(liscat))):
                                print(f'{posicion}  {item.nombre}')
                            cat=input('Seleccione una Categoria\n')
                            if cat=='':
                                pass
                            else:
                                while True:
                                    os.system('cls')
                                    productos=Producto.lista_productos_por_categoria(liscat[int(cat)])
                                    for item in productos:
                                        datos=item.obtener_datos_producto()
                                        print(f'ID: {item.iden},  Descripcion: {item.descripcion},  Precio: {item.precio},  Stock: {item.stock},  Marca: {item.marca},  Modelo: {item.modelo}')
                                    selectproductos=input('Seleccione la ID de un Producto para modificarlo\n')
                                    if selectproductos!='':
                                        while True:
                                            os.system('cls')
                                            modificarproducto=Producto.get(Producto.iden == selectproductos)
                                            print(f'ID: {modificarproducto.iden},  Descripcion: {modificarproducto.descripcion},  Precio: {modificarproducto.precio},  Stock: {modificarproducto.stock},  Marca: {modificarproducto.marca},  Modelo: {modificarproducto.modelo}')
                                            modificar=input(
                                                '1. Modificar Descripcion\n'
                                                '2. Modificar Precio \n'
                                                '3. Modificar Stock\n'
                                                '4. Modificar Marca\n'
                                                '5. Modificar Modelo\n'
                                                '6. Añadir Categoria\n'
                                                '7. Eliminar Categoria\n'
                                                '8. Eliminar Producto \n'
                                                'ENTER. Salir \n'
                                            )
                                            if modificar == '1':
                                                os.system('cls')
                                                modificarproducto.modificar_descripcion(input('Descripcion: \n'))
                                            elif modificar == '2':
                                                os.system('cls')
                                                modificarproducto.modificar_precio(float(input('Precio: \n')))
                                            elif modificar == '3':
                                                os.system('cls')
                                                modificarproducto.modificar_stock(int(input('Stock: \n')))
                                            elif modificar == '4':
                                                os.system('cls')
                                                modificarproducto.modificar_marca(input('Marca: \n'))
                                            elif modificar == '5':
                                                os.system('cls')
                                                modificarproducto.modificar_modelo(input('Modelo: \n'))
                                            elif modificar == '6':
                                                while True:
                                                    os.system('cls')
                                                    liscat=Categoria.obtener_lista_categorias()
                                                    liscatproducto=modificarproducto.get_categorias()
                                                    liscatfiltrada=[categoria for categoria in liscat if categoria not in liscatproducto]
                                                    for item in liscatfiltrada:
                                                        print(f'ID: {item.iden}  Nombre: {item.nombre}')
                                                    cat=input('Seleccione una Categoria\n')
                                                    if cat=='':
                                                        break
                                                    else:
                                                        modificarproducto.agregar_categoria(Categoria.get(Categoria.iden==cat))
                                            elif modificar == '7':
                                                while True:
                                                    os.system('cls')
                                                    listcat=modificarproducto.get_categorias()
                                                    for item in listcat:
                                                        print(f'ID: {item.iden}  Nombre: {item.nombre}')
                                                    cat=input('Seleccione una Categoria\n')
                                                    if cat=='':
                                                        break
                                                    else:
                                                        modificarproducto.eliminar_categoria(Categoria.get(Categoria.iden==cat))
                                            elif modificar == '8':
                                                os.system('cls')
                                                modificarproducto.eliminar_producto()
                                            elif modificar == '':
                                                os.system('cls')
                                                break
                                        
                                    else:
                                        break
                        if adminentrada2 == '3':
                            os.system('cls')
                            buscar=input('Buscar\n')
                            if buscar=='':
                                pass
                            else:
                                while True:
                                    os.system('cls')
                                    productos = Producto.lista_productos_por_cariterio(buscar)
                                    for item in productos:
                                        print(f'ID: {item.iden},  Descripcion: {item.descripcion},  Precio: {item.precio},  Stock: {item.stock},  Marca: {item.marca},  Modelo: {item.modelo}')
                                    selectproductos=input('Seleccione la ID de un Producto para modificarlo\n')
                                    if selectproductos!='':
                                        while True:
                                            os.system('cls')
                                            modificarproducto=Producto.get(Producto.iden == selectproductos)
                                            print(f'ID: {modificarproducto.iden},  Descripcion: {modificarproducto.descripcion},  Precio: {modificarproducto.precio},  Stock: {modificarproducto.stock},  Marca: {modificarproducto.marca},  Modelo: {modificarproducto.modelo}')
                                            modificar=input(
                                                '1. Modificar Descripcion\n'
                                                '2. Modificar Precio \n'
                                                '3. Modificar Stock\n'
                                                '4. Modificar Marca\n'
                                                '5. Modificar Modelo\n'
                                                '6. Añadir Categoria\n'
                                                '7. Eliminar Categoria\n'
                                                '8. Eliminar Producto \n'
                                                'ENTER. Salir \n'
                                            )
                                            if modificar == '1':
                                                os.system('cls')
                                                modificarproducto.modificar_descripcion(input('Descripcion: \n'))
                                            elif modificar == '2':
                                                os.system('cls')
                                                modificarproducto.modificar_precio(float(input('Precio: \n')))
                                            elif modificar == '3':
                                                os.system('cls')
                                                modificarproducto.modificar_stock(int(input('Stock: \n')))
                                            elif modificar == '4':
                                                os.system('cls')
                                                modificarproducto.modificar_marca(input('Marca: \n'))
                                            elif modificar == '5':
                                                os.system('cls')
                                                modificarproducto.modificar_modelo(input('Modelo: \n'))
                                            elif modificar == '6':
                                                while True:
                                                    os.system('cls')
                                                    liscat=Categoria.obtener_lista_categorias()
                                                    liscatproducto=modificarproducto.get_categorias()
                                                    liscatfiltrada=[categoria for categoria in liscat if categoria not in liscatproducto]
                                                    for item in liscatfiltrada:
                                                        print(f'ID: {item.iden}  Nombre: {item.nombre}')
                                                    cat=input('Seleccione una Categoria\n')
                                                    if cat=='':
                                                        break
                                                    else:
                                                        modificarproducto.agregar_categoria(Categoria.get(Categoria.iden==cat))
                                            elif modificar == '7':
                                                while True:
                                                    os.system('cls')
                                                    listcat=modificarproducto.get_categorias()
                                                    for item in listcat:
                                                        print(f'ID: {item.iden}  Nombre: {item.nombre}')
                                                    cat=input('Seleccione una Categoria\n')
                                                    if cat=='':
                                                        break
                                                    else:
                                                        modificarproducto.eliminar_categoria(Categoria.get(Categoria.iden==cat))
                                            elif modificar == '8':
                                                os.system('cls')
                                                modificarproducto.eliminar_producto()
                                            elif modificar == '':
                                                os.system('cls')
                                                break
                                        
                                    else:
                                        break
                        if adminentrada2 == '':
                            break

                    
                if adminentrada == '2':
                    while True:
                        os.system('cls')
                        categoriaentrada=input(
                            '1. Lista Categorias\n'
                            '2. Agregar Categoria\n'
                            'ENTER. Salir \n'
                        )
                    
                        if categoriaentrada == '1':
                            while True:
                                os.system('cls')
                                listacategorias=Categoria.obtener_lista_categorias()
                                for item in listacategorias:
                                    print(f'ID: {item.iden}  Nombre: {item.nombre}')
                                selectcarcategoria=input('Seleccione la ID de una Categoria para modificarla\n')
                                if selectcarcategoria=='':
                                    break
                                else:
                                    os.system('cls')
                                    modificarcategoria=Categoria.get(Categoria.iden==selectcarcategoria)
                                    modificar=input(
                                        '1. Modificar Nombre\n'
                                        '2. Eliminar Categoria\n'
                                    )
                                    if modificar == '1':
                                        os.system('cls')
                                        modificarnombrecategoria=input('Nombre:\n')
                                        if modificarnombrecategoria!='':
                                            modificarcategoria.modificar_categoria(modificarnombrecategoria)
                                    elif modificar == '2':
                                        os.system('cls')
                                        modificarcategoria.eliminar_categoria()

                        elif categoriaentrada == '2':
                            os.system('cls')
                            nombrecategorianueva=input('Nombre:\n')
                            if nombrecategorianueva !='':
                                Categoria.agregar_categoria(nombrecategorianueva)

                        else: break


                elif adminentrada == '':
                    os.system('cls')
                    break



        else:
            pass
        
    elif entrada == '2':
        os.system('cls')
        Cliente.alta_cliente(
            input('Ingrese su Nombre:\n'),
            input('Ingrese su Apellido:\n'),
            input('Ingrese su Telefono:\n'),
            input('Ingrese su Documento:\n'),
            input('Ingrese su Mail:\n'),
            input('Ingrese su Direccion:\n'),
            input('Ingrese su Nombre de Usuario:\n'),
            input('Ingrese su Contraseña:\n'),
        )

    elif entrada == '3':
        os.system('cls')
        Administrador.alta_administrador(
            input('Ingrese su Nombre:\n'),
            input('Ingrese su Apellido:\n'),
            input('Ingrese su Telefono:\n'),
            input('Ingrese su Documento:\n'),
            input('Ingrese su Mail:\n'),
            input('Ingrese su Nombre de Usuario:\n'),
            input('Ingrese su Contraseña:\n'),
        )

    elif entrada == '':
        os.system('cls')
        break

    else:
        os.system('cls')
