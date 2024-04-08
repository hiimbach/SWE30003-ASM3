import sys 
sys.path.append('.')
from logic import Account 
from pages import Page
from ui import RegisterUI

class RegisterPage(Page):
    def __init__(self):
        self.__register = Account()
        self.__register_ui = RegisterUI()
        
    def run(self):
        self.__register_ui.inform()
        account_info = self.__register_ui.interact()
        
        # If account_info is None, then the user wants to go back to the main page
        if account_info == None:
            return
        
        # If account_info is not None, then the user wants to register
        else:
            name, email, password, phone, age, address = account_info
            self.__register.add_account(name, age, address, phone, email, password)
            
if __name__ == "__main__":
    register_page = RegisterPage()
    register_page.run()
        
        