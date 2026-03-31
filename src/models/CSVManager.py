import os
import csv as csv
from Inventory import InventoryManager as InventoryManager
from Product import Product as Product
class CSVManager:
    def __init__(self, path: str):
        self.path: str = path

    def save_csv(self, inventory: list[Product], path:str, include_header: bool=True):
        """Save the inventory to a csv file.

        Args:
            inventory (list[Product]): Have to be a list that only contains the object Product
            path (str): The path where the file will be saved.
            include_header (bool, optional): True for incluide a header, False to not. Defaults to True.
        """         
        if inventory == []:
            print("Inventario vacio. No hay datos que guardar")
        else:
            try:
                with open(self.path, mode="w", encoding="utf-8", newline=";") as f:
                    w = csv.writer(f, delimiter=",")
                    if include_header:
                        w.writerow(["nombre", "precio", "cantidad", "costo"])
                    for product in inventory:
                        w.writerow([
                            product.getName(),
                            product.getPrice(),
                            product.getQuantity(),
                            product.getCost()
                        ])
                print(f"Inventario guardado en: {path}")
            except FileNotFoundError:
                print("Archivo no encontrado")
            except Exception as e:
                print(e)

    def load_csv(self, inventory:list[Product], path:str):
        if inventory != []:
            print("El inventario tiene datos. Debe eliminarlos antes de intentar cargar un csv.")
        elif not (os.path.exists(path)):
            print("El path no existe")
        else: 
            try:
                with open(self.path, mode="r")