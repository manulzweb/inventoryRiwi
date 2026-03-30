from src.models.Product import Product

class Inventory:
    def __init__(self):
        self.__inventory = []
        self.total_quantity = 0
        self.total_cost= 0
    
    def getInventory(self) -> list[Product]:
        return self.__inventory

    #Crear
    def addProduct(self, product: Product):
        self.getInventory().append(product)
        self.updateInventory()

    def removeProduct(self, name):
        for i, product in enumerate(self.getInventory()):
            if product.getName() == name:
                return self.__inventory.pop(i)
        raise ValueError("Producto no encontrado")
    
    def updateInventory(self):
        self.setTotalCost(sum(p.getCost() for p in self.getInventory()))
        self.setTotalQuantity(sum(p.getQuantity() for p in self.getInventory()))

    # #Para buscar producto por id
    # def searchById(self, idToSearch):
    #     for i, product in enumerate(self.__inventory):
    #         if product.getId() == idToSearch:
    #             return product
    #     return None

    def searchByName(self, name_to_search):
        for i, product in enumerate(self.getInventory()):
            if product.getName()==name_to_search:
                return product
        return None
    
    #Getters
    def getTotalCost(self):
        return self.__total_cost

    def getTotalQuantity(self):
        return self.__total_quantity

    def setTotalCost(self, new_cost):
        self.__total_cost = new_cost

    def setTotalQuantity(self, new_quantity):
        self.__total_quantity = new_quantity