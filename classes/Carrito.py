from Producto import Producto
class Carrito:
    def __init__(self) -> None:
        self.__productos:list[Producto] = []     
        self.__total:float = 0.0

    def get_total(self) -> float:
        self.set_total()
        return self.__total
    def set_total(self) -> None:
        total=0.0
        for x in self.__productos:
            total+=x.get_precio()
        self.__total = total

    def get_id_producto(self, posicion) -> int:
        if posicion<len(self.__productos):
            return self.__productos[posicion].get_ide()
        else:
            return None
        
    def get_descripcion_producto(self, posicion) -> str:
        if posicion<len(self.__productos):
            return self.__productos[posicion].get_descripcion()
        else:
            return None
        
    def get_precio_producto(self, posicion) -> float:
        if posicion<len(self.__productos):
            return self.__productos[posicion].get_precio()
        else:
            return None
        
    def get_stock_producto(self, posicion) -> int:
        if posicion<len(self.__productos):
            return self.__productos[posicion].get_stock()
        else:
            return None
        
    def get_marca_producto(self, posicion) -> str:
        if posicion<len(self.__productos):
            return self.__productos[posicion].get_marca()
        else:
            return None
        
    def get_modelo_producto(self, posicion) -> str:
        if posicion<len(self.__productos):
            return self.__productos[posicion].get_modelo()
        else:
            return None

    def añadir_producto_al_carrito(self, producto:Producto) -> None:
        self.__productos.append(producto)