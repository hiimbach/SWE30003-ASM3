import os 
import sys 
if os.path.abspath(os.getcwd()) not in sys.path:
    sys.path.append(os.path.abspath(os.getcwd()))

from utils.ui import CatalogUI
from logic import Inventory, Cart
from pages import ProductPage


class CatalogPage():
    def __init__(self) -> None:
        self.__ui = CatalogUI()
        self.__inventory = Inventory()
        self.__cart = Cart()

    def run(self):
        keep_running = True
        while keep_running:
            # Show catalog
            os.system('clear')
            self.__ui.inform()
            option = self.__ui.interact()
            
            if isinstance(option, int):
                chosen_product = self.__inventory.products()[option-1]
                os.system('clear')
                
                # Ask user for amount of product
                in_cart_amount = self.__cart.amount_of(chosen_product)
                product_page = ProductPage(chosen_product, in_cart_amount)
                product_page.run()
            
            else:
                keep_running = False
                

if __name__ == "__main__":
    catalog_page = CatalogPage()
    catalog_page.run()