import os
from logic import QueryDB

absolute_path = os.path.dirname(__file__)

class Account():
    def __init__(self) -> None:
        self.__query = QueryDB('db')
        
    def authenticate(self, email, password):
        '''
        Check whether the email and password are correct
        '''
        email = email.strip()
        account = self.__query.read('account', query=f"result=table[table['email'] == '{email}']")
        if len(account) == 0:
            return False
        # Retrieve password from the db
        saved_password = account['password'].values[0]
        
        # Check password
        if saved_password == password:
            user_id = account['user_id'].values[0]
            with open("db/current_user.txt", "w") as f:
                f.write(str(user_id))
            return True 
        else:
            return False
    
    def add_account(self, username: str, age: int, address: str, phone: str, email: str, password: str) -> str:
        '''
        Add new account to the db
        '''
        # Retrieve new user_id
        account_table = self.__query.read('account', query='result=table')
        user_id = account_table['user_id'].max() + 1
        
        # Add account to the db
        self.__query.modify('account', query=f"table.loc[len(table)] = [{user_id}, '{username}', {age}, '{address}', '{phone}', '{email}', '{password}', 'customer']")
        
        return "Success"
    
    def check_email_exist(self, email: str) -> bool:
        '''
        Check whether the email is in the db
        '''
        account_table = self.__query.read('account', query='result=table')
        if email in account_table['email'].values:
            return True
        else:
            return 
        
    def logout(self):
        '''
        Logout the current user
        '''
        with open("db/current_user.txt", "w") as f:
            f.write("")
        return True