from src.models.Product import Product
from src.models.Inventory import InventoryManager as Inventory
from src.views.View import View
import time

class Controller:

    def __init__(self, model: Inventory, view: View):
        self.modelList: Inventory = model
        self.view: View = view

    def start(self):
        self.view.clearTerminal()
        self.view.welcomeView()
        time.sleep(1)
        sw = True
        while sw:
            try:
                self.view.menuView()
                option = self.view.validateInteger("Eliga una opción: ")
                match option:
                    case 1:
                        self.addProductMenu()
                    case 2:
                        self.showProducts()
                    case 3:
                        self.view.clearTerminal()
                        if(self.modelList.getInventory() == []):
                            self.view.errorGetAll()
                        else:
                            name = self.view.captureName()
                            product = self.modelList.searchByName(name)
                            if(product == None):
                                self.view.errorExistence()
                            else:
                                self.view.showMessage(product.getData())
                    case 4:
                        self.view.clearTerminal()
                        if(self.modelList.getInventory() == []):
                            self.view.errorGetAll()
                        else:
                            name = self.view.captureName()
                            product = self.modelList.searchByName(name)
                            if(product == None):
                                self.view.errorExistence()
                            else:
                                productDeleted = self.modelList.removeProduct(name)
                                self.view.showMessage("Se ha eliminado correctamente el producto: "+productDeleted.getData())
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7: 
                        sw = False
                    case _:
                        self.view.errorOption()
            except Exception as e:
                self.view.showMessage(f"Error: {e}")

    def addProduct(self) -> Product:
        data: dict[str, str | int | float] = (self.view.captureData())
        productoCreated = Product(str(data["name"]), float(data["price"]), int(data["quantity"]))
        self.modelList.addProduct(productoCreated)
        return productoCreated

    def addProductMenu(self):
        sw1 = True
        while sw1:
            self.view.clearTerminal()
            pCreated = self.addProduct()
            time.sleep(0.1)
            self.view.showMessageColor("¡Producto creado y agregado al inventario con exito!\n"+pCreated.getData(), "green")
            time.sleep(0.1)
            res:str = self.view.validateString("¿Desea agregar otro producto? (s/n): ")
            if res.lower() != "n" and res.lower() != "s":
                res = self.view.validateString("Respuesta Incorrecta. ¿Desea agregar otro producto? (s/n): ")
            elif res.lower() == "n":
                sw1 = False
            else:
                sw1 = True
            time.sleep(0.3)

    def getProduct(self):
        product = self.modelList.searchByName(self.view.captureName())
        if product == None:
            self.view.errorExistence()
        else: 
            self.view.showMessage(product.getData())

    def showProducts(self):
        self.view.clearTerminal()
        products = self.modelList.getInventory()
        if not products:
            self.view.errorGetAll()
        else:
            validation = False
            while not validation:
                res = self.view.validateInteger("¿Desea mostrar un producto (0) o todos? (1): ")
                if res != 0 and res != 1:
                    res = self.view.validateInteger("Respuesta Incorrecta. ¿Desea mostrar un producto (0) o todos? (1): ")
                elif res == 0:
                    self.getProduct()
                    validation=True
                else:
                    self.view.showAllView(products, self.modelList.getTotalCost())
                    validation=True

    def saveCsv(self):
        print(f"Funcionalidad en desarrollo...")

    def loadCsv(self):
        print(f"Funcionalidad en desarrollo...")
