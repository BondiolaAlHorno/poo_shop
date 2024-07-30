class pago:
    def __init__(self,metPago,numTar,estado):
        self.__metPago:bool=metPago
        self.__numTar:int=numTar
        self.__estado:bool=estado

    def getmetPago(self)->bool:
        return self.__metPago
    def setmetPago(self,metPago:bool):
        self.__metPago:metPago

    def getnumTar(self)->int:
        return self.__numTar
    def setnumTar(self,numTar:int):
        self.__numTar:numTar

    def getestado(self)->bool:
        return self.__estado
    def setestado(self,estado:bool):
        self.__estado:estado