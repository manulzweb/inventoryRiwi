from src.models.Product import Product
from functools import reduce
class InventoryManager:
    def __init__(self):
        """Constructor para inventario."""
        self.__inventory: list[Product] = []
        self.__total_quantity: int = 0
        self.__total_cost: float= 0
        self.__most_expensive: Product
        self.__most_stocked: Product
    
    def getInventory(self) -> list[Product]:
        """Getter de inventario.
        Returns:
            list[Product]: Lista de objetos producto.
        """
        return self.__inventory

    #Crear
    def addProduct(self, product: Product):
        """Agrega un producto a la lista de productos. Luego calcula las estadisticas.
        Args:
            Product: Objeto de clase Product
        """
        self.getInventory().append(product)
        self.calStats()

    def removeProduct(self, name: str):
        """Busca el producto y si lo encuentra elimina un producto de la lista de productos.
        Args:
            string (str): Nombre del producto.
        Returns:
            Product: Producto eliminado
        """
        for i, product in enumerate(self.getInventory()):
            if product.getName() == name:
                return self.__inventory.pop(i)
        raise ValueError("Producto no encontrado")
    
    def searchByName(self, name_to_search: str):
        """Busca un producto por nombre.
        Args:
            string (str): Nombre del producto.
        Returns:
            Product: Producto eliminado
        """
        for product in self.getInventory():
            if product.getName()==name_to_search:
                return product
        return None
    
    def updateProduct(self, name: str, new_price: float, new_quantity: int):
        """Actualiza el precio y la cantidad de un producto.
        Args:
            string (str): Nombre del producto.
        """
        res = self.searchByName(name)
        if res == None:
            raise ValueError("Producto no encontrado")
        else: 
            res.setPrice(new_price)
            res.setQuantity(new_quantity)

    def calStats(self):
        """Calcula las estadisticas y las asigna mediante set. Para obtenerlas debes llamar al getter."""
        self.setTotalCost(sum(p.getCost() for p in self.getInventory()))
        self.setTotalQuantity(sum(p.getQuantity() for p in self.getInventory()))
        self.setMostExpensive(reduce(lambda p1, p2: p1 if p1.getPrice() > p2.getPrice() else p2, self.getInventory()))
        self.setMostExpensive(reduce(lambda p1, p2: p1 if p1.getPrice() > p2.getPrice() else p2, self.getInventory()))

    #Getters
    def getTotalCost(self) -> float:
        """Obtiene el costo total
        Returns:
            float: Costo total del inventario
        """
        return self.__total_cost

    def getTotalQuantity(self) -> int:
        """Obtiene la cantidad total
        Returns:
            int: Cantidad de productos en el inventario
        """
        return self.__total_quantity
    
    def getMostExpensive(self) -> Product:
        """Obtiene el producto más caro de todos los productos
        Returns:
            Product: Instancia más cara de la lista.
        """
        return self.__most_expensive

    def getMostStocked(self) -> Product:
        """Obtiene el producto más caro de todos los productos
        Returns:
            Product: Instancia con más stock de la lista.
        """
        return self.__most_stocked

    def setTotalCost(self, new_cost: float):
        """"""
        self.__total_cost = new_cost

    def setTotalQuantity(self, new_quantity: int):
        self.__total_quantity = new_quantity
    
    def setMostExpensive(self, new_most_expensive: Product):
        self.__most_expensive = new_most_expensive
    
    def setMostStocked(self, new_most_stocked: Product):
        self.new_most_stocked = new_most_stocked