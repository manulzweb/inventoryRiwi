from src.models.Product import Product
from src.models.InventoryManager import InventoryManager as Inventory
from src.views.View import View
from src.services.csv_manager import load_csv, save_csv

class Controller:
    """Class to manage the flow between inventory model and view."""

    def __init__(self, model: Inventory, view: View):
        """Initialize controller with model and view."""
        self.modelInv: Inventory = model
        self.view: View = view

    def start(self):
        """Start the application main loop and menu."""
        self.view.clearTerminal()
        self.view.welcomeView()
        sw = True
        while sw:
            try:
                self.view.menuView()
                option = self.view.validateInteger("Eliga una opción: ")
                match option:
                    case 1:
                        self.view.clearTerminal()
                        self.addProductMenu()
                    case 2:
                        self.view.clearTerminal()
                        self.showProducts()
                    case 3:
                        self.view.clearTerminal()
                        self.showOneProduct()
                    case 4:
                        self.view.clearTerminal()
                        self.updateProduct()
                    case 5:
                        self.view.clearTerminal()
                        self.deleteProduct()
                    case 6:
                        self.view.clearTerminal()
                        self.showStats()
                    case 7:
                        self.view.clearTerminal()
                        self.saveCsv()
                    case 8:
                        self.view.clearTerminal()
                        self.loadCsv()
                    case 9: 
                        self.view.clearTerminal()
                        self.view.closeView()
                        sw = False
                    case _:
                        self.view.clearTerminal()
                        self.view.errorOption()
            except Exception as e:
                self.view.errorException(e)

    def addProduct(self) -> Product:
        """Capture data from view and add a new product to model.

        Returns:
            Product: Created product object.
        """
        data: dict[str, str | int | float] = (self.view.captureData())
        productCreated = self.modelInv.createProduct(data)
        self.modelInv.addProduct(productCreated)
        return productCreated

    def addProductMenu(self):
        """Menu loop to add multiple products."""
        sw = True
        while sw:
            pCreated = self.addProduct()
            self.view.showMessageColor("¡Producto creado y agregado al inventario con exito!\n"+pCreated.getData(), "green")
            sw = self.view.ask_to_confirm("¿Desea agregar otro producto?")

    def getProduct(self, name:str):
        """Search for a product by name and handle errors.

        Args:
            name (str): Product name to find.

        Returns:
            Product: Found product or None.
        """
        if self.modelInv.isEmpty():
            self.view.errorGetAll()
        else:
            product = self.modelInv.searchByName(name)
            if product is None:
                self.view.errorExistence()
            return product

    def showOneProduct(self):
        name = self.view.captureName()
        product = self.getProduct(name)
        if product:
            self.view.showMessageColor(product.getData(), "cyan")

    def showProducts(self):
        """Show one or all inventory products based on user input."""
        if self.modelInv.isEmpty():
            self.view.errorGetAll()
        else:
            sw = True
            res = self.view.validateInteger("¿Desea mostrar un producto (0) o todos? (1): ")
            while sw:
                if not (res == 0 or res == 1):
                    res = self.view.validateInteger("Respuesta Incorrecta. ¿Desea mostrar un producto (0) o todos? (1): ")
                elif res == 0:
                    self.showOneProduct()
                    sw=False
                else:
                    self.view.showAllView(self.modelInv.getInventory())
                    sw=False

    def updateProduct(self):
        """Update price and quantity of an existing product."""
        if self.modelInv.isEmpty():
            self.view.errorGetAll()
        else:
            name = self.view.captureName()
            product = self.getProduct(name)
            if(product):
                price = self.view.capturePrice()
                quantity= self.view.captureQuantity()
                self.modelInv.updateProduct(name, price, quantity)
                self.view.showMessageColor("Producto actualizado: ", "green")
                self.view.showMessage(product.getData())

    def deleteProduct(self):
        """Remove a product from inventory by name."""
        if self.modelInv.isEmpty():
            self.view.errorGetAll()
        else:
            name = self.view.captureName()
            product = self.getProduct(name)
            if(product):
                productDeleted = self.modelInv.removeProduct(name)
                self.view.showMessage("Se ha eliminado correctamente el producto: "+productDeleted.getData())

    def showStats(self):
        """Show general inventory statistics."""
        stats = self.modelInv.getStats()
        self.view.showMessageColor("Estadisticas:", "yellow")
        self.view.showMessageColor(f"Costo Total: ${stats[0]}", "yellow")
        self.view.showMessageColor(f"Cantidad Total: {stats[1]}", "yellow")
        self.view.showMessageColor(f"Producto más costoso: Nombre: {stats[2][0]} | Precio: ${stats[2][1]}", "yellow")
        self.view.showMessageColor(f"Producto con más stock: {stats[3][0]} | Cantidad: {stats[3][1]}", "yellow")

    def saveCsv(self):
        """Save inventory data into a CSV file."""
        if self.modelInv.isEmpty():
            self.view.errorGetAll()
        else:
            inv = self.modelInv.getInventory()
            path = self.view.validateString("Ingrese la ruta donde quiera guardar el csv: ")
            if not ( path.lower().endswith(".csv")):
                path+=".csv"
            sw = True
            while sw:
                try:
                    save_csv(inv,path)
                    self.view.showMessageColor(f"Datos guardados con éxito en la ruta: {path}", "green")
                    sw = False
                except (FileNotFoundError) as e:
                    self.view.showMessageColor(f"{e}: Archivo no creado", "red")
                except IsADirectoryError as e:
                    self.view.showMessageColor(f"{e}: La ruta termina en un directorio", "red")
                except Exception as e:
                    self.view.errorException(e)
                    sw=False

    def rowSkippedMessage(self, value: int):
        """Show message about skipped rows in CSV loading.

        Args:
            value (int): Number of skipped rows.
        """
        if value == 0:
            self.view.showMessageColor("¡No se encontró ninguna fila dañada! 0 Omitidas.", "green")
        elif value > 0 and value <= 3:
            self.view.showMessageColor(f"Se encontraron {value} fallas en filas, y fueron omitidas", "yellow")
        elif value > 3:
            self.view.showMessageColor(f"Actividad Critica: Se encontraron {value} fallas en las filas, y fueron totalmente omitidas.", "red")
        
    def overWrite(self, data_list: list[dict[str, str | int | float]]):
        """Clear inventory and replace with data list."""
        self.modelInv.clearInv()
        for data in data_list:
            new_product = self.modelInv.createProduct(data)
            self.modelInv.addProduct(new_product)
        self.view.showMessageColor("La sobreescritura fue exitosa.", "green")
        return "Reemplazo"

    def fusionWrite(self, data_list: list[dict[str, str | int | float]]):
        """Merge data list with current inventory."""
        for data in data_list:
            name_to_search: str = str(data["nombre"])
            product = self.modelInv.searchByName(name_to_search)
            if product is not None:
                prev_quantity = product.getQuantity()
                quantity = prev_quantity+int(data["cantidad"])
                self.modelInv.updateProduct(product.getName(), float(data["precio"]), quantity)
            else:
                new_product = self.modelInv.createProduct(data)
                self.modelInv.addProduct(new_product)
        self.view.showMessageColor("La fusion fue exitosa.", "green")
        return "Fusión"

    def loadCsv(self):
        """Load data from CSV and choose between overwrite or fusion."""
        path = self.view.validateString("Ingrese la ruta del archivo csv a cargar: ")
        try:
            data_list, skipped = load_csv(path)
            self.rowSkippedMessage(skipped)
            res = self.view.ask_to_confirm("¿Sobrescribir inventario actual?")
            if res:
                mode = self.overWrite(data_list)
            else:
                self.view.showMessageColor("Política: suma de cantidades y actualización de precio si difiere","yellow")
                mode = self.fusionWrite(data_list)
            self.view.showMessageColor(f"Productos cargados: {len(data_list)} | Filas omitidas: {skipped} | Modo: {mode}","cyan")
        except UnicodeDecodeError:
            self.view.showMessageColor("Error UnicodeDecodeError: Error en la codificacion.", "red")
        except Exception as e:
            self.view.errorException(e)