from utils.ui import ProductCatalogUI
from logic.product import Product
from logic.cart import Cart

class ProductPage:
    def __init__(self, product: Product, in_cart: int) -> None:
        self.__ui = ProductCatalogUI(product, in_cart_amount=in_cart)
        self.__product = product
        self.__cart = Cart()
    
    def run(self):
        self.__ui.inform()
        amount_option = self.__ui.interact()
        
        # Add product to cart 
        self.__cart.modify_product(self.__product, amount_option)
        