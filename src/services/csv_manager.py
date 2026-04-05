import os
import csv as csv
from src.models.Product import Product as Product

def save_csv(inventory: list[Product], path:str, include_header: bool=True):
    """Save the inventory to a csv file.

    Args:
        inventory (list[Product]): Have to be a list that only contains the object Product
        path (str): The path where the file will be saved.
        include_header (bool, optional): True for incluide a header, False to not. Defaults to True.
    """         
    with open(path, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["nombre", "precio", "cantidad",]
        w = csv.DictWriter(file, fieldnames=fieldnames)
        if include_header:
            w.writeheader()
        for product in inventory:
            w.writerow({
                "nombre": product.getName(),
                "precio": product.getPrice(),
                "cantidad":product.getQuantity()
                })
def load_csv(path:str):
    """This function load a csv

    Args:
        path (str): path of the csv file

    Raises:
        FileNotFoundError: the file doesnt was found
        PermissionError: the user dont have permissions
        ValueError: File doesnt have fieldnames
        LookupError: Broken row

    Returns:
        list[dict[str, str | int | float]]: List with dicts inside
        int: total skipped broken rows
    """ 
    error_rows = 0
    if not (os.path.exists(path)):
        raise FileNotFoundError(f"El archivo no existe en la ruta: {path}")
    if not (os.access(path, os.R_OK)):
        raise PermissionError("No tienes permisos para leer el archivo")

    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",") #intentar quitar el linedeliminator
        
        if reader.fieldnames != ["nombre", "precio", "cantidad"]:
            raise ValueError("El archivo csv no tiene encabezado")
        data: dict[str, str | int | float]
        templist: list[dict[str, str | int | float]] = []
        for row in reader:
            try:
                if row["nombre"].strip() == "":
                        raise ValueError("Nombre vacío")
                if len(row) != 3 or float(row["precio"]) < 0 or int(row["cantidad"]) < 0 :
                    raise ValueError("Fila dañada")
                data = {"nombre": row["nombre"], "precio": float(row["precio"]), "cantidad": int(row["cantidad"])}
                templist.append(data)
            except ValueError:
                error_rows+=1
        return templist, error_rows
