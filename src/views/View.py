from colorama import Fore, Style
import os

class View:

    def __init__(self, controller = None):
        pass

    def clearTerminal(self):
        os.system('clear')

    def welcomeView(self):
            print(Fore.WHITE+ "╔════════════════════════════════╗")
            print(f"║           Bienvenido           ║")
            print(f"╠════════════════════════════════╣" + Fore.RESET)
        
    def menuView(self):
        print(Fore.WHITE+f"║ 1. Registrar un nuevo producto ║")
        print(f"║ 2. Ver todos los productos     ║")
        print(f"║ 3. Buscar producto por id      ║")
        print(f"║ 4. Eliminar un producto        ║")
        print(f"║ 5. Guardar en csv              ║")
        print(f"║ 6. Cargar un csv               ║")
        print(f"║ 7. Cerrar programa             ║")
        print(f"╚════════════════════════════════╝"+ Fore.RESET)
        
    def ValidateOption(self, op):
        while not (op > 0 and op<=7):
            op = self.errorOption()
        return op
    
    def errorOption(self):
        print(Fore.RED+"╔════════════════════════════════╗")
        print(f"║            ¡¡ERROR!!           ║")
        print(f"║   ¡Digite una opcion valida!   ║")
        print(f"╚════════════════════════════════╝"+ Fore.RESET)
        op = self.validateData(f"Eliga una opción: ", int)
        return op

    def errorNegative(self, id):
        print(Fore.RED+f"╔════════════════════════════════╗")
        print(f"║ ¡ERROR!  ¡Digite un id valido! ║")
        print(f"║  ID #{id} no puede ser negativo.  ║")
        print(f"╚════════════════════════════════╝" + Fore.RESET)
        id = self.validateData(f"Id : ", int)
        return id

    def errorAdd(self):
        print(Fore.RED+"Error, el producto no ha sido creado."+ Fore.RESET)
    
    def errorGetAll(self):
        print(Fore.RED+"Error, no se ha podido listar los productos."+ Fore.RESET)
    
    def errorExistence(self):
        print(Fore.RED+f"╔════════════════════════════════╗")
        print(f"║     Producto no encontrado     ║")
        print(f"║No existe un producto con ese ID║")
        print(f"╚════════════════════════════════╝"+Fore.RESET)
        
    def successAdd(self, producto):
        print(Fore.GREEN+f"Se agregó exitosamente el producto: {producto.getData()}"+Fore.RESET)

    def successExistence(self, producto):
        if producto.getId() < 10:
            idFormateado = "0"+str(producto.getId())
        else: 
            idFormateado = producto.getId()
        print(f"╔════════════════════════════════╗")
        print(f"║      Producto encontrado       ║")
        print(f"║  El producto con ID #{idFormateado} es:    ║")
        print(f"╚════════════════════════════════╝")
        
    def captureData(self):
        self.clearTerminal()
        """Captura los datos: Nombre, precio, cantidad. Y retorna una tupla en su respectivo orden. """
        name = self.validateData(f"Ingrese el nombre del producto: ", str)
        category = self.validateData(f"Ingrese el nombre del producto: ", str)
        price = self.validateData(f"¿Cuanto cuesta una unidad de {name}? ", float)
        quantity = self.validateData(f"¿Cuantas unidades de {name} registraras? ", int)
        return name,category,price,quantity
    
    def validateData(self, mensaje, tipoDeDato): #Funcion capaz de validar todos los datos, ingresa el mensaje y luego con input lo lee, seguidamente lo valida, y por ultimo lo retorna si es que no salta excepcion
        validacion = False
        data = 0
        while not validacion:
            try:
                data = tipoDeDato(input(mensaje))
                validacion = True
            except ValueError:
                print(f"Error: El tipo de dato debe ser {tipoDeDato}")
        return data

    def captureId(self):
        id = self.validateData(f"Ingrese el id del producto: ", int)
        while not (id > 0):
            id = self.errorNegative(id)
        return id
    
    def captureName(self):
        name = self.validateData(f"Ingrese el name del producto: ", str)
        while not (name == ""):
            id = self.errorNegative(name)
        return name

    def showProductView(self, data):
        print(data)

    def showAllView(self, productos, quantity):
        print(f"Info Lista:\nCantidad de Productos: {len(productos)}\nCosto Total: {quantity}\nLista:")
        for p in productos:
            print(f"Id: {p.getId()} | Nombre: {p.getName()} | Precio: {p.getPrice()} | Cantidad {p.getQuantity()} | Costo Total: {p.getCost()}")
    
    def closeView(self):
        print(f"╔════════════════════════════════╗")
        print(f"║       Cerrando Programa...     ║")
        print(f"║  Gracias por usar el programa! ║")
        print(f"╚════════════════════════════════╝")
        return False