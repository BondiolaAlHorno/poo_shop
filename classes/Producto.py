from Categoria import Categoria
class Producto:
    def __init__(self, descripcion:str, precio:float, stock:int, marca:str, modelo:str) -> None:
        self.__ide:int = None
        self.__descripcion:str = descripcion
        self.__precio:float = precio
        self.__stock:int = stock
        self.__marca:str = marca
        self.__modelo:str = modelo
        self.__categoria:list[Categoria] = None

    def get_ide(self) -> int:
        return self.__ide
    def set_ide(self, ide:int) -> None:
        self.__ide = ide

    def get_descripcion(self) -> str:
        return self.__descripcion
    def set_descripcion(self, descripcion:str) -> None:
        self.__descripcion = descripcion

    def get_precio(self) -> float:
        return self.__precio
    def set_precio(self, precio:float) -> None:
        self.__precio = precio

    def get_stock(self) -> int:
        return self.__stock
    def set_stock(self, stock:int) -> None:
        self.__stock = stock

    def get_marca(self) -> str:
        return self.__marca
    def set_marca(self, marca:str) -> None:
        self.__marca = marca

    def get_modelo(self) -> str:
        return self.__modelo
    def set_modelo(self, modelo:str) -> None:
        self.__modelo = modelo

    def get_id_categoria(self) -> list:
        lista_id = []
        for id_categoria in self.__categoria:
            lista_id.append(id_categoria.get_id())
        return lista_id
    def set_categoria(self, categoria:list) -> None:
        self.__categoria = categoria