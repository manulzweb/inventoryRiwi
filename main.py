from src.controllers.Controller import Controller
from src.models.Inventory import Inventory
from src.views.View import View

def main():
    model = Inventory()
    view = View()
    ctrl = Controller(model, view)

    ctrl.start()

if __name__ == "__main__":
    main()