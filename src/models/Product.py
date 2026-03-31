class Product:
    __name = ""
    __price =0
    __quantity=0
    __cost=0

    def __init__(self, name: str = "", price: float = 0, quantity: int = 0):
        self.__name: str= name
        self.__price: float=price
        self.__quantity: int=quantity
        self.__cost: float=self.getCost()
    
    def calCost(self):
        self.__cost=self.__price*self.__quantity
    
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getQuantity(self) -> int:
        return self.__quantity

    def getCost(self) -> float:
        self.calCost()
        return self.__cost

    def setName(self, name: str):
        self.__name=name

    def setPrice(self, price: float):
        self.__price=price

    def setQuantity(self, quantity: int):
        self.__quantity=quantity

    def getData(self):
        return f"Nombre: {self.getName()} | Precio: ${self.getPrice()} | Cantidad: {self.getQuantity()} | Costo total: ${self.getCost()}"