from utils.ui import UI 
from logic import UserManagement

class MainUI(UI):
    def __init__(self) -> None:
        super().__init__("Main Menu")
        self.__user_management = UserManagement()
        
    def description(self):
        curr_user = self.__user_management.get_current_user()
        if curr_user == None:
            self.print("Welcome to All Your Healthy Food Store!", "yellow")
            self.print("Please login or register to order.")
        else:
            self.print(f"Welcome to All Your Healthy Food Store, {curr_user.name}!", "yellow")
            
        self.print("Please select the following options:")
        self.print("1. Login")
        self.print("2. Register")
        self.print("3. Catalog")
        self.print("4. Cart")
        self.print("5. Logout")
        
    def interact(self):
        option = self.get_range(range_=5, text="Select an option: ")
        return option