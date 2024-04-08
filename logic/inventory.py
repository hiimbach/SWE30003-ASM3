from typing import Union
from logic import Product, QueryDB


class Inventory:
    def __init__(self) -> None:
        self.__query = QueryDB("db")   
        
    def reduce_amount(self, product: Product, amount: int):
        '''
        Reduce the amount of the product in the inventory
        '''
        if amount == product.amount:
            self.__query.modify('inventory', f"table = table.drop(table[table['name'] == '{product.name}'].index)")
        else:
            self.__query.modify('inventory', f"table.loc[table['name'] == '{product.name}', 'amount'] -= {amount}")
        
    def products(self):
        '''
        Return the list of products in the inventory
        '''
        # product function is used to have up-to-date product list
        product_list = []
        
        table = self.__query.read('inventory', 'result = table')
        for i in range(len(table)):
            product_list.append(Product.from_series(table.loc[i]))    
        return product_list
    
    def amount_of(self, product: Union[Product, str]):
        '''
        Get the amount of the product in the inventory
        '''
        if isinstance(product, Product):
            product_name = product.name
        else:
            product_name = product
            
        amount = self.__query.read('inventory', f"result = table[table['name'] == '{product_name}']['amount']")
        if len(amount) > 0:
            return amount.values[0]
        
    def price_of(self, product: Union[Product, str]):
        '''
        Get the price of the product in the inventory
        '''
        if isinstance(product, Product):
            product_name = product.name
        else:
            product_name = product
            
        price = self.__query.read('inventory', f"result = table[table['name'] == '{product_name}']['price']")
        if len(price) > 0:
            return price.values[0]

    def from_product_name(self, product_name: str):
        '''
        Get the product based on its name
        '''
        product = self.__query.read('inventory', f"result = table[table['name'] == '{product_name}']")
        if len(product) > 0:
            return Product.from_series(product.iloc[0])
        else:
            return None