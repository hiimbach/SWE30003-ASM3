from tabulate import tabulate

from logic import Cart, Inventory
from utils.ui import UI

class CartUI(UI):
    def __init__(self) -> None:
        super().__init__("Cart")
        self.__cart = Cart()
        self.__inventory = Inventory()
        
    def description(self):
        data = self.__cart.current()
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
        self.print(f"Total: {'{:.2f}'.format(self.__cart.total())}$", color="yellow")
        
    def interact(self):
        keep = True
        while keep:
            self.print("1. Modify Product Amounts")
            self.print("2. Checkout")
            
            option = self.get(text="Choose an option based on the number, or type Q to quit: ")
                
            if option.lower() == "q":
                keep = False
            else:
                try:
                    option = int(option)
                except ValueError:
                    self.print("Invalid option. Please try again.", color="red")
                    continue
                if option in [1, 2]:
                    return option
                
                else:
                    self.print("Invalid option. Please try again.", color="red") 
                    continue 

        return 0