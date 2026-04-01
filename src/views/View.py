from colorama import Fore
from src.models.Product import Product as Product
import os, time

class View:

    def __init__(self):
        pass

    def clearTerminal(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def welcomeView(self):
            print(Fore.WHITE+ "╔════════════════════════════════╗")
            print(f"║           Bienvenido           ║")
            print(f"╚════════════════════════════════╝" + Fore.RESET)
        
    def menuView(self):
        print(Fore.WHITE+ "╔════════════════════════════════╗")
        print(f"║ 1. Agregar un nuevo producto   ║")
        print(f"║ 2. Mostrar producto(s)         ║")
        print(f"║ 3. Buscar producto por nombre  ║")
        print(f"║ 4. Actualizar producto         ║")
        print(f"║ 5. Eliminar producto           ║")
        print(f"║ 5. Estadísticas producto       ║")
        print(f"║ 7. Guardar CSV                 ║")
        print(f"║ 8. Cargar CSV                  ║")
        print(f"║ 9. Cerrar programa             ║")
        print(f"╚════════════════════════════════╝"+ Fore.RESET)
        
    def errorOption(self):
        print(Fore.RED+"╔════════════════════════════════╗")
        print(f"║            ¡¡ERROR!!           ║")
        print(f"║   ¡Digite una opcion valida!   ║")
        print(f"╚════════════════════════════════╝"+ Fore.RESET)
        
    def errorAdd(self):
        print(Fore.RED+"Error, el producto no ha sido creado."+ Fore.RESET)
    
    def errorGetAll(self):
        print(Fore.RED+"Error, lista vacia"+ Fore.RESET)
    
    def errorException(self, e: Exception):
        print(Fore.RED+f"Error de tipo {type(e).__name__}: {e}"+ Fore.RESET)
    
    def errorExistence(self):
        print(Fore.RED+f"╔════════════════════════════════╗")
        print(f"║     Producto no encontrado     ║")
        print(f"║No existe un producto con ese ID║")
        print(f"╚════════════════════════════════╝"+Fore.RESET)
        
    def successAdd(self, product: Product):
        print(Fore.GREEN+f"Se agregó exitosamente el producto: {product.getData()}"+Fore.RESET)
    
    def read(self, msg: str):
        return input(msg)

    def validateString(self, msg: str) -> str:
        """Captura y valida cadenas."""
        validation = False
        string = ""
        while not validation:
            try:
                string = str(self.read(f"{msg}"))
                validation = True
            except ValueError:
                print("Debe introducir un texto")
        return string
    
    def validateInteger(self, msg: str) -> int:
        """Captura y valida enteros."""
        validation = False
        integer: int = 0
        while not validation:
            try:
                integer = int(self.read(f"{msg}"))
                validation = True
            except ValueError:
                print("Debe introducir un numero entero")
        return integer
    
    def validateFloat(self, msg: str) -> float:
        """Captura y valida flotantes."""
        validation = False
        fl: float = 0
        while not validation:
            try:
                fl = float(self.read(f"{msg}"))
                validation = True
            except ValueError:
                print("Debe introducir un numero flotante")
        return fl
    
    def captureName(self):
        name = self.validateString("Nombre del producto: ")
        if len(name) < 2:
            raise ValueError("El nombre del producto es muy corto, debe ser mayor a 2 caracteres.")
        if len(name) > 50:
            raise ValueError("El nombre del producto es muy largo, debe ser menor a 50 caracteres.")
        return name
    
    def capturePrice(self):
        price = float(self.validateFloat(f"Precio por unidad: "))
        if price < 0: 
            raise ValueError("El precio no puede ser negativo.")
        return price

    def captureQuantity(self):
        quantity = self.validateInteger(f"Cantidad de unidades: ")
        if quantity < 0: 
            raise ValueError("El precio no puede ser negativo.")
        return quantity

    def captureData(self) -> dict[str, str | float | int]:
        self.clearTerminal()
        validation = False
        while not validation:
            try: 
                time.sleep(0.4)
                self.showMessage("Ingrese los siguientes datos: ")
                time.sleep(0.2)
                name: str = self.captureName()
                time.sleep(0.2)
                price: float = self.capturePrice()
                time.sleep(0.2)
                quantity: int = self.captureQuantity()
                time.sleep(0.2)
                validation = True
                return {
                    "name": name,
                    "price": price,
                    "quantity" :quantity
                        }
            except ValueError as a:
                self.showMessage(f"Error: {a}")
        return {}
                
    def showMessage(self, data: str):
        print(data)

    def showMessageColor(self, data: str, color: str):
        match color:
            case "red":
                print(Fore.RED+data+Fore.RESET)
            case "green":
                print(Fore.GREEN+data+Fore.RESET)
            case "yellow":
                print(Fore.YELLOW+data+Fore.RESET)
            case _:
                pass

    def showAllView(self, products: list[Product], total_cost: float):
        print(Fore.WHITE+"Lista:")
        for p in products:
            print(Fore.CYAN+f"Nombre: {p.getName()} | Precio: {p.getPrice()} | Cantidad {p.getQuantity()} | Costo Total: ${p.getCost()}"+Fore.RESET)
    
    def closeView(self):
        print(Fore.LIGHTMAGENTA_EX+"╔════════════════════════════════╗")
        print(f"║       Cerrando Programa...     ║")
        print(f"║  Gracias por usar el programa! ║")
        print(f"╚════════════════════════════════╝"+Fore.RESET)
        return False