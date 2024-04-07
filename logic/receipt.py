from logic import User, QueryDB, UserManagement

class Receipt:
    def __init__(self, invoice_id) -> None:
        self.__query = QueryDB("db") 
        self.__invoice_id = invoice_id
        self.__user_management = UserManagement()
        
    def user_info(self):
        # print(self.__invoice_id)
        invoice_info = self.__query.read('transaction', f"result=table[table['invoice_id'] =={self.__invoice_id}]")
        user_id = invoice_info['user_id'].values[0]
        user_info = self.__user_management.get_user_from_id(user_id)
        
        return user_info
    
    def total_money(self):
        invoice_info = self.__query.read('transaction', f"result=table[table['invoice_id'] =={self.__invoice_id}]")
        all_subtotals = invoice_info['subtotal']
        return sum(all_subtotals)
    
    def transaction_date(self):
        invoice_info = self.__query.read('transaction', f"result=table[table['invoice_id'] =={self.__invoice_id}]")
        return invoice_info['time'].values[0]
        
    