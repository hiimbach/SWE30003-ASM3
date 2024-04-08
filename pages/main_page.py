import sys 
sys.path.append('.')

from pages import CartPage, CatalogPage, LoginPage, RegisterPage, Page
from logic import Account
from ui import MainUI

class MainPage(Page):
    def __init__(self) -> None:
        self.__ui = MainUI()
        self.__account = Account()
        
    def run(self):
        keep_running = True
        while keep_running:
            self.__ui.inform()
            option = self.__ui.interact()
            
            if option == None:
                return
            else:
                if option == 1:
                    # To login page
                    login_page = LoginPage()
                    login_page.run()
                
                elif option == 2:
                    # To register page
                    register_page = RegisterPage()
                    register_page.run()
                
                elif option == 3:
                    # To catalog page
                    catalog_page = CatalogPage()
                    catalog_page.run()
                    
                elif option == 4:
                    # To cart page
                    cart_page = CartPage()
                    cart_page.run()
                    
                elif option == 5:
                    # Logout
                    self.__account.logout()
                    
                else:
                    self.__ui.print("Invalid option", "red")
                    
if __name__ == "__main__":
    main_page = MainPage()
    main_page.run()