from src.controllers.Controller import Controller
from src.models.InventoryManager import InventoryManager as Inventory
from src.views.View import View
from src.services.CSVManager import CSVManager

def main():
    model = Inventory()
    view = View()
    csvManager = CSVManager()
    ctrl = Controller(model, view, csvManager)

    ctrl.start()

if __name__ == "__main__":
    main()