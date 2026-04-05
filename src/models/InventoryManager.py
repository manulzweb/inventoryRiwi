from src.models.Product import Product
from functools import reduce
class InventoryManager:
    def __init__(self):
        """Inventory Model Constructor, contains a list: inventory and anothers atributtes"""
        self.__inventory: list[Product] = []
        self.__total_quantity: int = 0
        self.__total_cost: float= 0
        self.__most_expensive: Product | None
        self.__most_stocked: Product | None
    
    def createProduct(self, data: dict[str, str | int | float]):
        """Create a product

        Args:
            data (dict[str, str  |  int  |  float]): Data of a product ready to be create

        Returns:
            Product: Returns the product that the function created.
        """
        productoCreated = Product(str(data["nombre"]), float(data["precio"]), int(data["cantidad"]))
        return productoCreated


    def addProduct(self, product: Product):
        """Add a product to the list: inventory atributte of the class inventoryManager.
        Also, recalculated the stats for each creation.
        Args:
            Product: A product created.
        """
        self.__inventory.append(product)
        self.calStats()

    def removeProduct(self, name: str):
        """Find a product and if it found it remove the product of list: inventory.
        Args:
            string (str): Name of a product
        Returns:
            Product: Removed product
        """
        for i, product in enumerate(self.getInventory()):
            if product.getName() == name:
                removed = self.__inventory.pop(i)
                self.calStats()
                return removed
        raise ValueError("Producto no encontrado")
    
    def searchByName(self, name_to_search: str):
        """Search a product by his name:
        Args:
            string (str): Name of the product to search.
        Returns:
            Product | None: If product exist return product, if not, return None
        """
        for product in self.getInventory():
            if product.getName().lower()==name_to_search.lower():
                return product
        return None
    
    def updateProduct(self, name: str, new_price: float, new_quantity: int):
        """Update the price and quantity of a product.
        Args:
            string (str): Name of product to update.
        """
        res = self.searchByName(name)
        if res is None:
            raise ValueError("Producto no encontrado")
        else: 
            res.setPrice(new_price)
            res.setQuantity(new_quantity)
            self.calStats()

    def clearInv(self):
        """
            Remove all products from the inventory.
        """
        self.__inventory.clear()

    def calStats(self):
        """Calculate and update inventory statistics.
        
        Raises:
            ValueError: If the inventory is empty.
        """
        inv = self.__inventory
        if self.isEmpty():
            self.setTotalCost(0)
            self.setTotalQuantity(0)
            self.setMostExpensive(None)
            self.setMostStocked(None)
        else:
            self.setTotalCost(sum(p.getCost() for p in inv))
            self.setTotalQuantity(sum(p.getQuantity() for p in inv))
            self.setMostExpensive(reduce(lambda p1, p2: p1 if p1.getPrice() > p2.getPrice() else p2, inv))
            self.setMostStocked(reduce(lambda p1, p2: p1 if p1.getQuantity() > p2.getQuantity() else p2, inv))
    
    def getStats(self):
        """Return a tuple with inventory statistics

        Returns:
            tuple: (total_cost,total_quantity, most_expensive, most_stocked)
        """
        most_expensive = self.getMostExpensive()
        most_stocked = self.getMostStocked()
        return (self.getTotalCost(), self.getTotalQuantity(), (most_expensive.getName(),most_expensive.getPrice()) if most_expensive is not None else ("N/A", 0), (most_stocked.getName(),most_stocked.getQuantity()) if most_stocked is not None else ("N/a", 0))
    
    def isEmpty(self):
        """ Just for know if invetory is empty.

        Returns:
            bool: True if atributte inventory == [], else False.
        """
        return self.getInventory() == []

    #Getters

    def getInventory(self) -> list[Product]:
        """Get inventory
        Returns:
            list[Product]: Product object list.
        """
        return self.__inventory

    def getTotalCost(self) -> float:
        """Get total cost
        Returns:
            float: Total cost of all products
        """
        return self.__total_cost

    def getTotalQuantity(self) -> int:
        """Return the total quantity
        Returns:
            int: Quantity of all products
        """
        return self.__total_quantity
    
    def getMostExpensive(self) -> Product | None:
        """Get the most expensive product
        Returns:
            Product: Most expensive product
        """
        return self.__most_expensive

    def getMostStocked(self) -> Product | None:
        """Get the most stocked products

        Returns:
            Product: Most stocked product
        """
        return self.__most_stocked
    
    #Setters
    def setInventory(self, new_inv: list[Product]):
        """Set an inventory

        Args:
            new_inv (list[Product]): new inventory to set
        """
        self.__inventory = new_inv

    def setTotalCost(self, new_cost: float):
        """Set the total cost

        Args:
            new_cost (float): new total cost to set
        """
        self.__total_cost = new_cost

    def setTotalQuantity(self, new_quantity: int):
        """Set the total quantity

        Args:
            new_quantity (int): new total quantity to set
        """ 
        self.__total_quantity = new_quantity
    
    def setMostExpensive(self, new_most_expensive: Product | None):
        """Set the most expensive product

        Args:
            new_most_expensive (Product): new most expensive to set
        """
        self.__most_expensive = new_most_expensive
    
    def setMostStocked(self, new_most_stocked: Product | None):
        """Set the most stocked product

        Args:
            new_most_stocked(Product): new most stocked to set
        """
        self.__most_stocked = new_most_stocked