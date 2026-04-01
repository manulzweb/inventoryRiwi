from src.models.Product import Product
from src.models.InventoryManager import InventoryManager as Inventory
from src.views.View import View
from src.services.CSVManager import CSVManager
import time

class Controller:

    def __init__(self, model: Inventory, view: View, csv_manager: CSVManager):
        self.modelInv: Inventory = model
        self.view: View = view
        self.csv_manager: CSVManager = csv_manager

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
                        product = self.getProduct(self.view.captureName())
                        self.view.showProduct(product.getData())
                    case 4:
                        self.updateProduct()
                    case 5:
                        self.view.clearTerminal()
                        if(self.modelInv.getInventory() == []):
                            self.view.errorGetAll()
                        else:
                            name = self.view.captureName()
                            product = self.modelInv.searchByName(name)
                            if(product == None):
                                self.view.errorExistence()
                            else:
                                productDeleted = self.modelInv.removeProduct(name)
                                self.view.showMessage("Se ha eliminado correctamente el producto: "+productDeleted.getData())
                    case 6:
                        pass
                    case 7:
                        self.saveCsv()
                    case 8:
                        pass
                    case 9: 
                        sw = False
                    case _:
                        self.view.errorOption()
            except Exception as e:
                self.view.errorException(e)

    def addProduct(self) -> Product:
        data: dict[str, str | int | float] = (self.view.captureData())
        productCreated = self.modelInv.createProduct(data)
        self.modelInv.addProduct(productCreated)
        return productCreated

    def addProductMenu(self):
        sw = True
        while sw:
            self.view.clearTerminal()
            pCreated = self.addProduct()
            time.sleep(0.1)
            self.view.showMessageColor("¡Producto creado y agregado al inventario con exito!\n"+pCreated.getData(), "green")
            time.sleep(0.1)
            res:str = self.view.validateString("¿Desea agregar otro producto? (s/n): ")
            if not (res.lower() == "n" or res.lower() == "s"):
                res = self.view.validateString("Respuesta Incorrecta. ¿Desea agregar otro producto? (s/n): ")
            if res.lower() == "n":
                sw = False
            time.sleep(0.3)

    def getProduct(self, name:str):
        if(self.modelInv.getInventory() == []):
            self.view.errorGetAll()
        else:
            product = self.modelInv.searchByName(name)
            if product == None:
                self.view.errorExistence()
            return product

    def showProducts(self):
        self.view.clearTerminal()
        validation = False
        while not validation:
            res = self.view.validateInteger("¿Desea mostrar un producto (0) o todos? (1): ")
            if res != 0 and res != 1:
                res = self.view.validateInteger("Respuesta Incorrecta. ¿Desea mostrar un producto (0) o todos? (1): ")
            elif res == 0:
                name = self.view.captureName()
                self.view.showMessage(self.getProduct(name).getData())
                validation=True
            else:
                self.view.showAllView(self.modelInv.getInventory(), self.modelInv.getTotalCost())
                validation=True

    def updateProduct(self):
        self.view.clearTerminal()
        if(self.modelInv.getInventory() == []):
            self.view.errorGetAll()
        else:
            name = self.view.captureName()
            product = self.modelInv.searchByName(name)
            if(product == None):
                self.view.errorExistence()
            else:
                price = self.view.capturePrice()
                quantity= self.view.captureQuantity()
                self.modelInv.updateProduct(name, price, quantity)
                self.view.showMessageColor("Producto actualizado: ", "green")
                self.view.showMessage(self.getProduct(name).getData())


    def saveCsv(self):
        switch = True
        inv = self.modelInv.getInventory()
        if  inv == []:
            raise ValueError("Inventario vacio. No hay datos que guardar")
        path = self.view.validateString("Ingrese el path donde quiera guardar el csv: ")
        while switch == True:
            try:
                self.csv_manager.save_csv(inv,path)
            except Exception as e:
                if not (type(e) == FileNotFoundError or type(e) == IsADirectoryError):
                    self.view.errorException(e)
                else:
                    self.view.errorException(e)
                    sw = True
                    res:str=self.view.validateString("¿Desea crear un archivo CSV? (s/n)")
                    while sw == True:
                        if not (res.lower() == "n" or res.lower() == "s"):
                            res = self.view.validateString("Respuesta Incorrecta. ¿Desea crear un archivo CSV? (s/n): ")
                        if res.lower() == "n":
                            switch = False
                        else:
                            name = self.view.validateString("Ingrese un nombre personalizado para su archivo csv (Si el campo queda vacio el nombre será inventory) (n: cancelar)")
                            if name == "n":
                                switch = False
                            if name == "":
                                path = self.csv_manager.createFileCSV(path)
                                self.view.showMessageColor(f"Archivo creado con exito! Intente nuevamente.\nRecuerde ingresar {name}.csv al final del path.\nEjemplo: {path}", "green")
                                sw = False
                            else: 
                                path = self.csv_manager.createFileCSV(path, name)
                                self.view.showMessageColor(f"Archivo creado con exito! Intente nuevamente.\nRecuerde ingresar {name}.csv al final del path.\nEjemplo: {path}", "green")
                                sw = False
            switch = False

    def loadCsv(self):
        path = self.view.validateString("Ingrese el path donde quiera guardar el csv: ")
        try:
            self.csv_manager.load_csv(path)
        except Exception as e:
            self.view.errorException(e)