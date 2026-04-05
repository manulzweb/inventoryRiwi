class Product:
    """Represents a product with name, price, quantity and total cost."""

    def __init__(self, name: str = "", price: float = 0, quantity: int = 0):
        """Initialize a product

        Args:
            name (str, optional): Name of product. Defaults to "".
            price (float, optional): Price per unit. Defaults to 0.
            quantity (int, optional): Number of units available. Defaults to 0.
        """
        self.__name: str= name
        self.__price: float=price
        self.__quantity: int=quantity
        self.__cost: float=self.getCost()
    
    def calCost(self):
        """Calculate and update the total cost of product
        """ 
        self.__cost=self.__price*self.__quantity
    
    def getName(self):
        """Return product's name

        Returns:
            str: Product's name
        """
        return self.__name
    
    def getPrice(self):
        """Return the product's price

        Returns:
            float: product's price per unit
        """
        return self.__price
    
    def getQuantity(self) -> int:
        """Return the product's quantity units

        Returns:
            int: quantity units of product
        """
        return self.__quantity

    def getCost(self) -> float:
        """Return the total cost (price * quantity).


        Returns:
            float: total cost
        """
        self.calCost()
        return self.__cost

    def setName(self, name: str):
        """Update the product name.

        Args:
            name (str): New product name
        """
        self.__name=name

    def setPrice(self, price: float):
        """Update the product price

        Args:
            price (float): New price per unit value
        """
        self.__price=price

    def setQuantity(self, quantity: int):
        """Update the product quantity

        Args:
            quantity (int): New quantity value
        """
        self.__quantity=quantity

    def getData(self):
        """Return formated string with product info

        Returns:
            str: Product info
        """
        return f"Nombre: {self.getName()} | Precio: ${self.getPrice()} | Cantidad: {self.getQuantity()} | Costo total: ${self.getCost()}"