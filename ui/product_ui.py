from ui import UI
from logic import Product, UserManagement

class ProductCatalogUI(UI):
    def __init__(self, product: Product, in_cart_amount) -> None:
        super().__init__("Product")
        self.__product = product
        self.__user_management = UserManagement()
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
        curr_user = self.__user_management.get_current_user()
        if curr_user == None:
            self.print("You need to login to add product to cart.")
            self.get("Type enter to continue: ")
            return 0
                    
        keep = True 
        while keep:
            self.print(f"You are currently having {self.__in_cart} of this product in your cart.", "yellow")
            option = self.get_range(range_=[-self.__in_cart, self.__product.amount-self.__in_cart],
                                    text="Type X you want to add more, -X if you want to reduce the amount, or type Q to quit: ")
            
            if option == None:
                return 0
            else:
                return option
                        
            