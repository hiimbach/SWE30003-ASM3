from utils.ui.base import UI
from logic.product import Product
from logic.cart import Cart

class ProductCatalogUI(UI):
    def __init__(self, product: Product, in_cart_amount) -> None:
        super().__init__("Product")
        self.__product = product
        if in_cart_amount == None:
            self.__in_cart = 0
        else:
            self.__in_cart = in_cart_amount
        
    def description(self):
        self.print(f"Product: {self.__product.name}", "yellow")
        self.print(f"Price: {self.__product.price}")
        self.print(f"Category: {self.__product.category}")
        self.print(f"Amount: {self.__product.amount}")
        self.print(f"Description: {self.__product.description}")
        
    def interact(self) -> int:
        # Ask user for amount of product
        keep = True
        while keep:
            self.print(f"You are currently having {self.__in_cart} of this product in your cart.", "yellow")
            option = self.get(text="Type X you want to add more, -X if you want to reduce the amount, or type Q to quit: ")
                
            if option.lower() == "q":
                keep = False
            else:
                try:
                    option = int(option)
                except ValueError:
                    self.print("Invalid option. Please try again.\n", color="red")
                    continue
                
                total = self.__in_cart + option
                if total < 0:
                    self.print("Invalid option. Please try again.", color="red")
                    continue
                elif total > self.__product.amount:
                    self.print("Sorry, we don't have enough product in stock.\n", color="red")
                    continue
                else:
                    return option
                    
        return 0
        
        