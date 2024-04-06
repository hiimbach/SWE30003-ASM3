from datetime import datetime
from logic import Cart, Product, Inventory, User, QueryDB, UserManagement

class Invoice:
    def __init__(self) -> None:
        self.__user_management = UserManagement()
        self.__user = self.__user_management.get_current_user()
        self.__cart = Cart()
        self.__query = QueryDB("db")

    def user_info(self):
        return self.__user
    
    def cart_info(self):
        return self.__cart
    
    def save_invoice(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S %d-%m-%Y")
        
        user_id = self.__user.user_id
        cart_info = self.__cart.current()
        
        invoice_history = self.__query.read('invoice', 'result=table')['invoice_id']
        if len(invoice_history) == 0:
            invoice_id = 1
        else:
            invoice_id = invoice_history.max() + 1
        
        for item in cart_info:
            prod_name = item['Product']
            amount = item['Amount']
            subtotal = item['Subtotal ($)']
            # import ipdb; ipdb.set_trace()
            
            self.__query.modify('invoice', f"table.loc[len(table)] = [{invoice_id}, {user_id}, '{prod_name}', {amount}, {subtotal}, '{formatted_time}']")

                
                
                
                
                