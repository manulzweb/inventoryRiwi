from colorama import Fore, init
init(autoreset=True)
from src.models.Product import Product as Product
import os, time

class View:
    """
    Class responsible for handling user interface interactions.
    """

    def __init__(self):
        """Initialize the View."""
        pass

    def clearTerminal(self):
        """
        Clear the terminal screen depending on the operative system.
        """
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def welcomeView(self):
        """
        Displays welcome message.
        """
        print(f"╔════════════════════════════════╗")
        print(f"║           Bienvenido           ║")
        print(f"╚════════════════════════════════╝" )

    def menuView(self):
        """
        Displays the main menu.
        """
        print(f"╔════════════════════════════════╗")
        print(f"║ 1. Agregar un nuevo producto   ║")
        print(f"║ 2. Mostrar producto(s)         ║")
        print(f"║ 3. Buscar producto por nombre  ║")
        print(f"║ 4. Actualizar producto         ║")
        print(f"║ 5. Eliminar producto           ║")
        print(f"║ 6. Estadísticas producto       ║")
        print(f"║ 7. Guardar CSV                 ║")
        print(f"║ 8. Cargar CSV                  ║")
        print(f"║ 9. Cerrar programa             ║")
        print(f"╚════════════════════════════════╝" )

    def errorOption(self):
        """
        Displays invalid option error.
        """
        self.showMessageColor("╔════════════════════════════════╗", "red")
        self.showMessageColor("║            ¡¡ERROR!!           ║", "red")
        self.showMessageColor("║   ¡Digite una opcion valida!   ║", "red")
        self.showMessageColor("╚════════════════════════════════╝", "red")

    def errorAdd(self):
        """
        Displays error when product is not created.
        """
        self.showMessageColor("Error, el producto no ha sido creado.", "red")

    def errorGetAll(self):
        """
        Displays error when list is empty.
        """
        self.showMessageColor("Error, lista vacia", "red")

    def errorException(self, exception: Exception):
        """Displays exception details.

        Args:
            exception (Exception): Exception raised during execution.
        """
        self.showMessageColor(f"Error de tipo {type(exception).__name__}: {exception}", "red")

    def errorExistence(self):
        """Displays error when product is not found."""
        self.showMessageColor("╔════════════════════════════════╗", "red")
        self.showMessageColor("║     Producto no encontrado     ║", "red")
        self.showMessageColor("║No existe un producto con ese ID║", "red")
        self.showMessageColor("╚════════════════════════════════╝", "red")

    def successAdd(self, product: Product):
        """Displays success message when product is added.

        Args:
            product (Product): Product successfully added.
        """
        self.showMessageColor(f"Se agregó exitosamente el producto: {product.getData()}", "green")

    def read(self, message: str):
        """Reads input from user.

        Args:
            message (str): Message to display to the user.

        Returns:
            str: User input.
        """
        return input(message)

    def validateString(self, message: str) -> str:
        """Captures and validates string input.

        Args:
            message (str): Message to display to the user.

        Returns:
            str: Validated string input.
        """
        is_valid = False
        value = ""
        while not is_valid:
            try:
                value = str(self.read(f"{message}")).strip()
                is_valid = True
            except ValueError:
                print("Debe introducir un texto")
        return value

    def validateInteger(self, message: str) -> int:
        """Captures and validates integer input.

        Args:
            message (str): Message to display to the user.

        Returns:
            int: Validated integer input.
        """
        is_valid = False
        value: int = 0
        while not is_valid:
            try:
                value = int(self.read(f"{message}"))
                is_valid = True
            except ValueError:
                print("Debe introducir un numero entero")
        return value

    def validateFloat(self, message: str) -> float:
        """Captures and validates float input.

        Args:
            message (str): Message to display to the user.

        Returns:
            float: Validated float input.
        """
        is_valid = False
        value: float = 0
        while not is_valid:
            try:
                value = float(self.read(f"{message}"))
                is_valid = True
            except ValueError:
                print("Debe introducir un numero flotante")
        return value

    def captureName(self):
        """Captures and validates product name.

        Returns:
            str: Validated product name.
        """
        name = self.validateString("Nombre del producto: ")
        if len(name) < 2:
            raise ValueError("El nombre del producto es muy corto, debe ser mayor a 2 caracteres.")
        if len(name) > 50:
            raise ValueError("El nombre del producto es muy largo, debe ser menor a 50 caracteres.")
        return name

    def capturePrice(self):
        """Captures and validates product price.

        Returns:
            float: Validated product price.
        """
        price = float(self.validateFloat(f"Precio por unidad: "))
        if price < 0:
            raise ValueError("El precio no puede ser negativo.")
        return price

    def captureQuantity(self):
        """Captures and validates product quantity.

        Returns:
            int: Validated product quantity.
        """
        quantity = self.validateInteger(f"Cantidad de unidades: ")
        if quantity < 0:
            raise ValueError("El precio no puede ser negativo.")
        return quantity

    def captureData(self) -> dict[str, str | float | int]:
        """Captures full product data.

        Returns:
            dict[str, str | float | int]: Dictionary containing product data.
        """
        self.clearTerminal()
        is_valid = False
        while not is_valid:
            try:
                self.showMessage("Ingrese los siguientes datos: ")
                name: str = self.captureName()
                price: float = self.capturePrice()
                quantity: int = self.captureQuantity()
                is_valid = True
                return {
                    "name": name,
                    "price": price,
                    "quantity": quantity
                }
            except ValueError as error:
                self.showMessage(f"Error: {error}")
        return {}

    def ask_to_confirm(self, message: str) -> bool:
        """Asks user for confirmation (yes/no).

        Args:
            message (str): Message to display.

        Returns:
            bool: True if user confirms, False otherwise.
        """
        while True:
            response = self.validateString(f"{message} (s/n): ").lower()
            if response == "s":
                return True
            if response == "n":
                return False

    def showMessage(self, data: str):
        """Displays a message.

        Args:
            data (str): Message to display.
        """
        print(data)

    def showMessageColor(self, data: str, color: str):
        """Displays a colored message.

        Args:
            data (str): Message to display.
            color (str): Color name (red, green, yellow).
        """
        match color:
            case "red":
                print(Fore.RED + data)
            case "green":
                print(Fore.GREEN + data)
            case "yellow":
                print(Fore.YELLOW + data)
            case "cyan":
                print(Fore.CYAN + data)

    def showAllView(self, products: list[Product], total_cost: float):
        """Displays all products.

        Args:
            products (list[Product]): List of products.
            total_cost (float): Total cost of all products.
        """
        print("Lista:")
        for product in products:
            self.showMessageColor(F"Nombre: {product.getName()} | Precio: {product.getPrice()} | Cantidad {product.getQuantity()} | Costo Total: ${product.getCost()}", "cyan")

    def closeView(self):
        """Displays closing message.

        Returns:
            bool: Always returns False to stop program execution.
        """
        print(Fore.LIGHTMAGENTA_EX + "╔════════════════════════════════╗")
        print(f"║       Cerrando Programa...     ║")
        print(f"║  Gracias por usar el programa! ║")
        print(f"╚════════════════════════════════╝" )
        return False