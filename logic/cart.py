from typing import Optional, Union, Dict
from logic import Product, QueryDB, Inventory


class Cart():
    def __init__(self) -> None:
        self.__query = QueryDB("db")
        self.__inventory = Inventory()    
        
    def current(self) -> Optional[Dict]:
        cart_df = self.__query.read('cart', 'result=table')
        cart_list = []
        
        for i in range(len(cart_df)):
            product_name = cart_df.loc[i]['product']
            amount = cart_df.loc[i]['amount']
            price = self.__inventory.price_of(product_name)
            subtotal = amount * price
            cart_list.append({"Product": product_name, "Amount": amount, "Price ($)": price, "Subtotal ($)": subtotal})
            
        return cart_list
    
    def amount_of(self, product: Union[Product, str]):
        if isinstance(product, Product):
            product_name = product.name
        else:
            product_name = product
            
        amount = self.__query.read('cart', f"result = table[table['product'] == '{product_name}']['amount']")
        if len(amount) > 0:
            return amount.values[0]
            
        
    def modify_product(self, product: Product, amount: int):
        product_name = product.name
        table = self.__query.read('cart', 'result=table')
        
        if product_name in table['product'].values:
            current_amount = self.__query.read('cart', f"result = table[table['product'] == '{product_name}']['amount']").values[0]
            if (current_amount + amount) > 0: 
                self.__query.modify('cart', f"table.loc[table['product'] == '{product_name}', 'amount'] += {amount}")
            else:
                if amount > 0:
                    self.__query.modify('cart', f"table = table[table['product'] != '{product_name}']")
        else:
            self.__query.modify('cart', f"table.loc[len(table)] = ['{product_name}', {amount}]")
            
            
    def check_amount(self, product: Union[Product, str]):
        if isinstance(product, Product):
            product_name = product.name
        else:
            product_name = product
            
        amount = self.__query.read('cart', f"result = table[table['product'] == '{product_name}']['amount']")
        if len(amount) > 0:
            return amount.values[0]
       
    def total(self):
        cart = self.current()
        total = 0
        for item in cart:
            total += item['Subtotal ($)']
        return total