from src.models.Product import Product
from src.models.InventoryManager import InventoryManager as Inventory
from src.views.View import View
from src.services.CSVManager import CSVManager

class Controller:

    def __init__(self, model: Inventory, view: View, csv_manager: CSVManager):
        self.modelInv: Inventory = model
        self.view: View = view
        self.csv_manager: CSVManager = csv_manager

    def start(self):
        self.view.clearTerminal()
        self.view.welcomeView()
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
                        if product != None:
                            self.view.showMessage(product.getData())
                    case 4:
                        self.updateProduct()
                    case 5:
                        self.deleteProduct()
                    case 6:
                        self.showStats()
                    case 7:
                        self.saveCsv()
                    case 8:
                        self.loadCsv()
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
            self.view.showMessageColor("¡Producto creado y agregado al inventario con exito!\n"+pCreated.getData(), "green")
            sw = self.view.ask_to_confirm("¿Desea agregar otro producto?")

    def getProduct(self, name:str):
        if self.modelInv.isEmpty():
            self.view.errorGetAll()
        else:
            product = self.modelInv.searchByName(name)
            if product == None:
                self.view.errorExistence()
            return product

    def showProducts(self):
        self.view.clearTerminal()
        if self.modelInv.isEmpty():
            self.view.errorGetAll()
        else:
            sw = True
            res = self.view.validateInteger("¿Desea mostrar un producto (0) o todos? (1): ")
            while sw:
                if not (res == 0 or res == 1):
                    res = self.view.validateInteger("Respuesta Incorrecta. ¿Desea mostrar un producto (0) o todos? (1): ")
                elif res == 0:
                    name = self.view.captureName()
                    product = self.getProduct(name)
                    if product:
                        self.view.showMessage(product.getData())
                    sw=False
                else:
                    self.view.showAllView(self.modelInv.getInventory(), self.modelInv.getTotalCost())
                    sw=False

    def updateProduct(self):
        self.view.clearTerminal()
        if self.modelInv.isEmpty():
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
                product = self.getProduct(name)
                if product:
                    self.view.showMessage(product.getData())

    def deleteProduct(self):
        self.view.clearTerminal()
        if self.modelInv.isEmpty():
            self.view.errorGetAll()
        else:
            name = self.view.captureName()
            product = self.modelInv.searchByName(name)
            if(product == None):
                self.view.errorExistence()
            else:
                productDeleted = self.modelInv.removeProduct(name)
                self.view.showMessage("Se ha eliminado correctamente el producto: "+productDeleted.getData())

    def showStats(self):
        self.modelInv.calStats()
        self.view.showMessageColor(f"Costo Total: {self.modelInv.getTotalCost()}", "yellow")
        self.view.showMessageColor(f"Cantidad Total: {self.modelInv.getTotalQuantity()}", "yellow")
        self.view.showMessageColor(f"Producto más costoso: {self.modelInv.getMostExpensive().getData()}", "yellow")
        self.view.showMessageColor(f"Producto con más stock: {self.modelInv.getMostStocked().getData()}", "yellow")


    def saveCsv(self):
        if self.modelInv.isEmpty():
            raise ValueError("Inventario vacio. No hay datos que guardar")
        inv = self.modelInv.getInventory()
        path = self.view.validateString("Ingrese el path donde quiera guardar el csv: ")
        sw = True
        while sw:
            try:
                self.csv_manager.save_csv(inv,path)
                self.view.showMessageColor("Datos guardados con éxito", "green")
                sw = False
            except (FileNotFoundError, IsADirectoryError) as e:
                self.view.showMessageColor("Pusiste un directorio o el archivo no fue encontrado", "red")
                res = self.view.ask_to_confirm("¿Desea crear un archivo CSV?")
                if not res:
                    sw=False
                else:
                    name = self.view.validateString("Ingrese un nombre personalizado para su archivo csv (Si el campo queda vacio el nombre será inventory) (n: cancelar)")
                    if name == "":
                        path = self.csv_manager.createFileCSV(path)
                    else: 
                        path = self.csv_manager.createFileCSV(path, name)
                    self.view.showMessageColor(f"Archivo creado con exito! Ejemplo: {path}", "green")
            except Exception as e:
                self.view.errorException(e)
                sw=False

    def rowSkippedMessage(self, value: int):
        if value == 0:
            self.view.showMessageColor("¡No se encontró ninguna fila dañada! 0 Omitidas.", "green")
        elif value > 0 and value <= 3:
            self.view.showMessageColor(f"Se encontraron {value} fallas en filas, y fueron omitidas", "yellow")
        elif value > 3:
            self.view.showMessageColor(f"Actividad Critica: Se encontraron {value} fallas en las filas, y fueron totalmente omitidas.", "red")
        

    def loadCsv(self):
        path = self.view.validateString("Ingrese el path donde quiera guardar el csv: ")
        try:
            data_list, skipped = self.csv_manager.load_csv(path)
            self.rowSkippedMessage(skipped)
            res = self.view.ask_to_confirm("¿Sobrescribir inventario a actual?")
            if res:
                #Overwrite
                self.modelInv.clearInv()
                for data in data_list:
                    new_product = self.modelInv.createProduct(data)
                    self.modelInv.addProduct(new_product)
                self.view.showMessageColor("La sobreescritura fue exitosa.", "green")
            else:
                #Fusion
                for data in data_list:
                    name_to_search: str = str(data["name"])
                    product = self.getProduct(name_to_search)
                    if product != None:
                         #If product is differente to None, product exist, we sum the previous quantity with the csv quantity, and price update
                        prev_quantity = product.getQuantity()
                        quantity = prev_quantity+int(data["quantity"])
                        self.modelInv.updateProduct(product.getName(), float(data["price"]), quantity)
                    else:
                        #If product doesnt exist, just create a product with dict data and add to the model
                        new_product = self.modelInv.createProduct(data)
                        self.modelInv.addProduct(new_product)
                self.view.showMessageColor("La fusion fue exitosa.", "green")
            self.view.showMessageColor(f"Productos cargados: {len(data_list)} | Filas omitidas: {skipped} ","cyan")
        except FileNotFoundError as e:
            self.view.errorException(e) #preguntarle a javi sobre esto. una excepcion que capture todos los raise? o varias para tener mas control.
        except PermissionError as e:
            self.view.errorException(e)
        except UnicodeDecodeError as e:
            self.view.errorException(e)
        except ValueError as e:
            self.view.errorException(e)
        except Exception as e:
            self.view.errorException(e)