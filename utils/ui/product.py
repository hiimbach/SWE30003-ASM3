from features.product import Product
from utils.ui.base import UI

class ProductUI(UI):
    def __init__(self, product: Product) -> None:
        super().__init__()
        self.__page_name = "Product"
        self.__product = product
        
    def description(self):
        self.print(f"Product: {self.__product.name}", "yellow")
        self.print(f"Price: {self.__product.price}")
        self.print(f"Category: {self.__product.category}")
        self.print(f"Amount: {self.__product.amount}")
        self.print(f"Description: {self.__product.description}")
        
    def main(self):
        keep = True
        while keep:
            option = self.get(text="Type the number you want, or type Q to quit: ")
                
            if option.lower() == "q":
                keep = False
            else:
                try:
                    option = int(option)
                except ValueError:
                    self.print("Invalid option. Please try again.", color="red")
                    continue
                
                if option > 0 and option <= self.__product.amount:
                    # NOTE: Add to cart
                    return True
                    
                else:
                    self.print("Invalid option. Please try again.", color="red") 
                    
        return False
        
        