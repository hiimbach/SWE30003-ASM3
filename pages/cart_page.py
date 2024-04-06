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
        keep_run = True
        
        while keep_run:
            os.system('clear')
            self.__ui.inform()
            option = self.__ui.interact()
        
            if isinstance(option, int): # Modify Product Amount
                # Chosen product from cart
                chosen_name = self.__cart.current()[option-1]["Product"]
                chosen_product = self.__inventory.from_product_name(chosen_name)
                
                # Ask user for amount of product
                in_cart_amount = self.__cart.amount_of(chosen_product)
                product_page = ProductPage(chosen_product, in_cart_amount)
                os.system('clear')
                product_page.run()
            
            elif isinstance(option, str):   # Checkout
                pass
                keep_run = False
            
            else:
                keep_run = False


if __name__ == "__main__":
    cart_page = CartPage()
    cart_page.run()