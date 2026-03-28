from src.models.Product import Product
from src.models.Inventory import Inventory
from src.views.View import View

class Controller:

    def __init__(self, model: Inventory, view):
        self.modelList: Inventory = model
        self.view = view

    def start(self):
        self.view.clearTerminal()
        sw = True
        while sw:
            # try:
                self.view.welcomeView()
                self.view.menuView()
                option = self.view.validateData("Eliga una opción: " , int)
                option = self.view.ValidateOption(option)
                match option:
                    case 1:
                        self.addProduct()

                    case 2:
                        self.getAll()
                    case 3:
                        self.view.clearTerminal()
                        id_prod = self.view.captureId()
                        product = self.modelList.searchById(id_prod)
                        if(self.modelList.productExist(product)):
                            self.view.showProductView(product.getData())
                        else:
                            self.view.errorExistence()
                    case 4:
                        id_prod = self.view.captureId()
                        productToRemove = self.modelList.searchById(id_prod)
                        if(self.modelList.productExist(productToRemove)):
                            productRemoved: Product = self.removeById(id_prod)
                            self.view.showProductView(productRemoved.getData())
                        else:
                            self.view.errorExistence()
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7: 
                        sw = False

    def addProduct(self):
        data: tuple[str | int | float] = (self.view.captureData())
        productoCreated = self.modelList.createProduct(data)
        res = self.modelList.addProduct(productoCreated)
        self.view.clearTerminal()
        if res:
            self.view.successAdd(productoCreated)
        else:
            self.view.errorAdd()

    def getAll(self): #probar
        self.view.clearTerminal()
        products = self.modelList.getInv()
        if not products:
            self.view.errorGetAll()
        else:
            self.view.showAllView(products, self.modelList.getTotalCost())

    def searchById(self, id) -> Product:
        productFound = Product()
        productFound = self.modelList.searchById(id)
        return productFound

    def searchByName(self, id) -> Product:
        productFound = Product()
        productFound = self.modelList.searchByName(id)
        return productFound

    def productExist(self, product):
        res = self.modelList.productExist(product)
        if res == False:
            self.view.errorExistence()
        else:
            self.view.successExistence(res)

    def removeById(self, id) -> Product:
        productFound = Product()
        productFound = self.modelList.searchById(id)
        if (self.modelList.productExist(productFound)):
            productRemoved = self.modelList.removeProduct(productFound.getId())
            return productRemoved
        return productFound

    def saveCsv(self):
        print(f"Funcionalidad en desarrollo...")

    def loadCsv(self):
        print(f"Funcionalidad en desarrollo...")
