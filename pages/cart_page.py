import sys
import os
sys.path.append('.')

from utils.ui import CartUI
from logic import Cart, Product, Inventory
from pages import ProductPage

class CartPage:
    def __init__(self) -> None:
        self.__cart = Cart()
        self.__ui = CartUI()
        self.__inventory = Inventory()  
    
    def run(self):
        os.system('clear')
        self.__ui.inform()
        option = self.__ui.interact()
        
        if isinstance(option, Product): # Modify Product Amounts
            chosen_product = self.__inventory.products()[option-1]
            os.system('clear')
            
            # Ask user for amount of product
            in_cart_amount = self.__cart.amount_of(chosen_product)
            product_page = ProductPage(chosen_product, in_cart_amount)
            product_page.run()
        
        else:   # Checkout
            pass


if __name__ == "__main__":
    cart_page = CartPage()
    cart_page.run()