from tabulate import tabulate

from logic import Cart, Inventory, UserManagement
from ui import UI

class CartUI(UI):
    def __init__(self) -> None:
        super().__init__("Cart")
        self.__cart = Cart()
        self.__user_management = UserManagement()  
        self.__current_user = self.__user_management.get_current_user()
        
    def description(self):
        if self.__current_user == None:
            self.print("You are not logged in. Please login to view your cart.")
            return
        else:
            data = self.__cart.current()
            print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
            self.print(f"Total: {'{:.2f}'.format(self.__cart.total())}$", color="yellow")
            self.print("\n*Some products may not be available in the inventory anymore.\nPlease recheck the amount of each product in the Catalog.")
        
    def interact(self):
        if self.__current_user == None:
            self.get("Type anything to continue: ")
            return None
        
        self.print("1. Modify Product Amounts")
        self.print("2. Checkout")
        
        option = self.get_range(range_=2, 
                                  text="Choose an option based on the number, or type Q to quit: ")
        
        if option == None:
            return None
        else:
            if option == 1:
                print(len(self.__cart.current()))
                # Ask for choosing product
                prod_id = self.get_range(range_=len(self.__cart.current()), 
                                           text="Choose a product based on the number, type Q to quit: ")
                return prod_id
            
            if option == 2:
                return "Checkout"