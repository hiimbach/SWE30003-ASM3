from tabulate import tabulate
import os

from utils.ui import UI
from logic import Inventory

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
        option = self.get_range(range_=len(self.__available_products()), 
                                text="Choose an product using the number, or type Q to quit: ")
                
        return option
                    