import sys 
sys.path.append('.')
from logic import Account 
from pages import Page
from utils.ui import RegisterUI

class RegisterPage(Page):
    def __init__(self):
        self.__register = Account()
        self.__register_ui = RegisterUI()
        
    def run(self):
        self.__register_ui.inform()
        account_info = self.__register_ui.interact()
        if account_info == None:
            return
        else:
            name, email, password, phone, age, address = account_info
            self.__register.add_account(name, age, address, phone, email, password)
            
if __name__ == "__main__":
    register_page = RegisterPage()
    register_page.run()
        
        