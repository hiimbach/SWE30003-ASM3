from tabulate import tabulate

from logic.cart import Cart
from logic.db import QueryDB
from utils.ui.base import UI
from logic.product import Product
from logic.inventory import Inventory

class CartUI(UI):
    def __init__(self) -> None:
        super().__init__("Product")
        self.__cart = Cart()
        self.__inventory = Inventory()
        
    def description(self):
        data = self.__cart.current()
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
        self.print(f"Total: {self.__cart.total()}$", color="yellow")
        
    def interact(self):
        keep = True
        while keep:
            self.print("1. Remove/Reduce Products")
            self.print("2. Add Products")
            self.print("3. Start Ordering")
            
            option = self.get(text="Choose an option based on the number, or type Q to quit: ")
                
            if option.lower() == "q":
                keep = False
            else:
                try:
                    option = int(option)
                except ValueError:
                    self.print("Invalid option. Please try again.", color="red")
                    continue
                if option <= 3 and option >= 1:
                    return option
                else:
                    self.print("Invalid option. Please try again.", color="red") 
                    continue 

        return 0