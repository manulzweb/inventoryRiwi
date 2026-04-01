import os
import csv as csv
from src.models.InventoryManager import InventoryManager as InventoryManager
from src.models.Product import Product as Product
from pathlib import Path
class CSVManager:
    def __init__(self):
        pass

    def createFileCSV(self, path:str, name:str="inventory") -> str:
        file_path = Path(path) / f"{name}.csv"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()
        return str(file_path)

    def save_csv(self, inventory: list[Product], path:str, include_header: bool=True):
        """Save the inventory to a csv file.

        Args:
            inventory (list[Product]): Have to be a list that only contains the object Product
            path (str): The path where the file will be saved.
            include_header (bool, optional): True for incluide a header, False to not. Defaults to True.
        """         
        if not (os.path.exists(path)):
            raise FileNotFoundError(f"El archivo no existe en la ruta: {path}")
        if not os.access(path, os.R_OK):
            raise PermissionError("No tienes permisos para escribir en el archivo")
        
        with open(path, mode="w") as file:
            fieldnames = ["nombre", "precio", "cantidad",]
            w = csv.DictWriter(file, fieldnames=fieldnames, lineterminator=";")
            if include_header:
                w.writeheader()
                for product in inventory:
                    w.writerow({
                        "nombre": product.getName(),
                        "precio": product.getPrice(),
                        "cantidad":product.getQuantity()
                    })

    def load_csv(self, path:str):
        error_rows = 0
        if not (os.path.exists(path)):
            raise FileNotFoundError(f"El archivo no existe en la ruta: {path}")
        if not (os.access(path, os.R_OK)):
            raise PermissionError("No tienes permisos para leer el archivo")

        with open(path, mode="r") as file:
            reader = csv.DictReader(file, delimiter=",", lineterminator=";")
            
            if reader.fieldnames != ["nombre", "precio", "cantidad"]:
                raise ValueError("El archivo csv no tiene encabezado")
            data: dict[str, str | int | float]
            templist: list[dict[str, str | int | float]] = []
            for row in reader:
                try:
                    if len(row) != 3:
                        raise ValueError("Fila dañada")
                    data = {"nombre": row["nombre"], "precio": float(row["precio"]), "cantidad": int(row["cantidad"])}
                    templist.append(data)
                except:
                    error_rows+=1
            return templist, error_rows
