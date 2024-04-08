from typing import Optional, Union, Dict
from logic import Product, QueryDB, Inventory, UserManagement


class Cart():
    def __init__(self) -> None:
        self.__query = QueryDB("db")
        self.__inventory = Inventory()    
        self.__user_management = UserManagement()
        self.__curr_user = self.__user_management.get_current_user()
        
        
    def current(self) -> Optional[Dict]:
        '''
        Return the current cart of the user
        The output is a list of dictionary with the following keys
        '''
        cart_df = self.__query.read('cart', f"result=table[table['user_id'] == {self.__curr_user.user_id}]")
        cart_list = []
        
        for i in range(len(cart_df)):
            product_name = cart_df.iloc[i]['product']
            amount = cart_df.iloc[i]['amount']
            price = self.__inventory.price_of(product_name)
            subtotal = amount * price
            cart_list.append({"ID": i+1, "Product": product_name, "Amount": amount, "Price ($)": price, "Subtotal ($)": subtotal})
            
        return cart_list
    
    def update(self):
        '''
        If the user A buy a product when it is in the cart of user B, the amount of the product in the cart of user B should be update in case the product does not have enough amount in the inventory
        '''
        # Check if the product still have the sufficient amount in the inventory
        for row in self.current():
            product_name = row['Product']
            amount = row['Amount']

            inven_amount = self.__query.read('inventory', f"result = table[table['name'] == '{product_name}']['amount'].values[0]")
            
            if inven_amount < amount:
                # Update the amount in the cart db
                self.modify_product(product_name, inven_amount-amount)
                        
        
    def modify_product(self, product: Union[Product, str], amount: int):
        '''
        Modify the amount of the product in the cart
        '''
        if isinstance(product, Product):
            product_name = product.name
        else:
            product_name = product
        
        # Get the current user id
        user_id = self.__curr_user.user_id
        table = self.__query.read('cart', f"result=table[table['user_id'] == {user_id}]")
        
        # Check if the product is in the cart
        if product_name in table['product'].values:
            current_amount = self.__query.read('cart', f"result = table[(table['product'] == '{product_name}') & (table['user_id'] == {user_id})]['amount']").values[0]
            
            # If the total amount is greater than 0, update the amount in the cart
            if (current_amount + amount) > 0: 
                self.__query.modify('cart', f"table.loc[(table['product'] == '{product_name}') & (table['user_id'] == {user_id}), 'amount'] += {amount}")
                
            # Else remove the product from the cart
            elif current_amount + amount == 0:
                    self.__query.modify('cart', f"table = table[~((table['product'] == '{product_name}') & (table['user_id'] == {user_id}))]")
        else:
            # Add the product to the cart with the amount
            if amount > 0:
                self.__query.modify('cart', f"table.loc[len(table)] = ['{product_name}', {amount}, {user_id}]")
            

    def amount_of(self, product: Union[Product, str]):
        '''
        Check the amount of the product in the cart
        '''
        if isinstance(product, Product):
            product_name = product.name
        else:
            product_name = product
        
        user_id = self.__curr_user.user_id 
        amount = self.__query.read('cart', f"result = table[(table['product'] == '{product_name}') & (table['user_id'] == {user_id})]['amount']")
        if len(amount) > 0:
            return amount.values[0]
       
    def total(self):
        '''
        Calculate the total price of the cart
        
        '''
        cart = self.current()
        total = 0
        for item in cart:
            total += item['Subtotal ($)']
        return total