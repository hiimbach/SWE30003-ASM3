import sys
import os
sys.path.append('.')

from utils.ui.cart import CartUI
from logic.cart import Cart

class CartPage:
    def __init__(self) -> None:
        self.__cart = Cart()
        self.__ui = CartUI()
    
    def run(self):
        os.system('clear')
        self.__ui.inform()
        option = self.__ui.interact()
        
if __name__ == "__main__":
    cart_page = CartPage()
    cart_page.run()