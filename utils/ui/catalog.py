from tabulate import tabulate
import os

from utils.ui.base import UI
from utils.ui.product import ProductCatalogUI
from logic.inventory import Inventory
from logic.product import Product

class CatalogUI(UI):
    def __init__(self) -> None:
        super().__init__("Catalog")
        self.__inventory = Inventory()
        
    def __available_products(self):
        # List of available products
        available_products = []
        for product in self.__inventory.products():
            if product.amount > 0:
                available_products.append(product)
        return available_products
        
    def description(self):
        data = []
        for i, product in enumerate(self.__available_products()):
            data.append({"ID": i+1,
                        "Product": product.name, 
                        "Price": product.price, 
                        "Quantity Left ": product.amount,
                        "Category": product.category})
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
                
    def interact(self):
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
                
                available_products = self.__available_products()
                if option in range(len(available_products)+1):
                    return option
                    
                else:
                    self.print("Invalid option. Please try again.", color="red") 
        return False
                
        