class Product:
    __name = ""
    __price =0
    __quantity=0
    __cost=0

    def __init__(self, name: str = "", price: float = 0, quantity: int = 0):
        name = name.strip()
        if len(name) < 2:
            raise ValueError("El nombre contiene menos de dos caracteres.")
        if price < 0:
            raise ValueError("El precio no puede ser negativo")
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        self.__name= name
        self.__price=price
        self.__quantity=quantity
        self.__cost=self.getCost()
    
    def calCost(self):
        self.__cost=self.__price*self.__quantity
    
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getQuantity(self) -> int:
        return self.__quantity

    def getCost(self):
        self.calCost()
        return self.__cost

    def setName(self, name):
        self.__price=name

    def setPrice(self, price):
        self.__price=price

    def setQuantity(self, price):
        self.__price=price

    def getData(self):
        return f" Nombre: {self.getName()} | Precio: ${self.getPrice()} | Cantidad: {self.getQuantity()} | Costo total: ${self.getCost()}"