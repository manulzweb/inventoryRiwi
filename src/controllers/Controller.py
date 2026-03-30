from src.models.Product import Product
from src.models.Inventory import Inventory
from src.views.View import View
import time

class Controller:

    def __init__(self, model: Inventory, view):
        self.modelList: Inventory = model
        self.view = view

    def start(self):
        self.view.clearTerminal()
        self.view.welcomeView()
        time.sleep(1.5)
        sw = True
        while sw:
            try:
                self.view.menuView()
                option = self.view.validateData("Eliga una opción: " , int)
                match option:
                    case 1:
                        self.addProduct()
                    case 2:
                        if(self.modelList.getInventory() == []):
                            self.view.errorGetAll()
                            return
                        self.getAll()
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

    def addProduct(self):
        data: tuple[str | int | float] = (self.view.captureData())
        productoCreated = Product(data[0], data[1], data[1])
        self.modelList.addProduct(productoCreated)

    def getAll(self):
        products = self.modelList.getInventory()
        if not products:
            self.view.errorGetAll()
        else:
            self.view.showAllView(products, self.modelList.getTotalCost())

    def saveCsv(self):
        print(f"Funcionalidad en desarrollo...")

    def loadCsv(self):
        print(f"Funcionalidad en desarrollo...")
