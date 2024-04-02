# Not having order ID at the moment 
from features.user import UserInfo
from features.product import Product

class Order:
    def __init__(self, user_info: UserInfo, product_container: Product) -> None:
        self.user_info = user_info
        self.product_container = product_container

    def total_amount(self):
        return self.product_container.price * self.product_container.amount
    
    
