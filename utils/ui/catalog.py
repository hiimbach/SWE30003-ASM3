from tabulate import tabulate
import os

from utils.ui.base import UI
from utils.ui.product import ProductUI
from features.catalog import Catalog
from features.product import Product

class CatalogUI(UI):
    def __init__(self, product: Product) -> None:
        super().__init__()
<<<<<<< Updated upstream
        self.__page_name = "Catalog"
        self.__catalog = catalog
=======
        self.page_name = "In-Cart Product"
        self.catalog = 
>>>>>>> Stashed changes
        
        # List of available products
        self.available_products = []
        for product in self.__catalog.products:
            if product.amount > 0:
                self.available_products.append(product)
        
    def description(self):
        self.print(f"Product: {self.product.name}")
        self.print(f"Price: {self.product.price}")
        self.print(f"Amount In cart: {self.amount}")
        self.print(f"Total Price: {self.total}")
                
    def main(self):
        keep = True
        while keep:
            option = self.get(text="Choose an product using the number, or type Q to quit: ")
                
            if option.lower() == "q":
                keep = False
            else:
                try:
                    option = int(option)
                except ValueError:
                    self.print("Invalid option. Please try again.", color="red")
                    continue
                
                if option in range(len(self.available_products)+1):
                    chosen_product = self.available_products[option-1]
                    product_ui = ProductUI(chosen_product)
                    os.system('clear')
                    product_ui.display()
                    return True
                    
                else:
                    self.print("Invalid option. Please try again.", color="red") 
        return False
                
        