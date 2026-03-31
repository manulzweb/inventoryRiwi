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
        print(f"║ 1. Registrar un nuevo producto ║")
        print(f"║ 2. Ver todos los productos     ║")
        print(f"║ 3. Buscar producto por nombre  ║")
        print(f"║ 4. Eliminar un producto        ║")
        print(f"║ 5. Guardar en csv              ║")
        print(f"║ 6. Cargar un csv               ║")
        print(f"║ 7. Cerrar programa             ║")
        print(f"╚════════════════════════════════╝"+ Fore.RESET)
        
    def errorOption(self):
        print(Fore.RED+"╔════════════════════════════════╗")
        print(f"║            ¡¡ERROR!!           ║")
        print(f"║   ¡Digite una opcion valida!   ║")
        print(f"╚════════════════════════════════╝"+ Fore.RESET)
        
    def errorAdd(self):
        print(Fore.RED+"Error, el producto no ha sido creado."+ Fore.RESET)
    
    def errorGetAll(self):
        print(Fore.RED+"Error, no se ha podido listar los productos."+ Fore.RESET)
    
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
        print(f"Info Lista:\nCantidad de Productos: {len(products)}\nCosto Total: {total_cost}\nLista:")
        for p in products:
            print(f"Nombre: {p.getName()} | Precio: {p.getPrice()} | Cantidad {p.getQuantity()} | Costo Total: ${p.getCost()}")
    
    def closeView(self):
        print(f"╔════════════════════════════════╗")
        print(f"║       Cerrando Programa...     ║")
        print(f"║  Gracias por usar el programa! ║")
        print(f"╚════════════════════════════════╝")
        return False