#estamos importando la libreria de peewee a nuestro proyecto 

from peewee import *
from Constructor import getdatabase

#importamos clase 
from BaseModel import BaseModel

#importamos las clases
from Persona import Persona
#desde el archivo persona.py importo la clase Persona(practica correcta que cada clase tenga su proipio archivo)
from Usuario import Usuario
from Administrador import Administrador
from Cliente import Cliente
from Carrito import Carrito
from Categoria import Categoria
from Pago import Pago
from Producto import Producto
from Venta import Venta
from ProductoCategoria import ProductoCategoria
from CarritoProducto import CarritoProducto
from VentaProducto import VentaProducto