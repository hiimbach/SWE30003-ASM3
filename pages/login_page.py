from utils.ui import LoginUI
from pages import Page
from logic import Account


class LoginPage(Page):
    def __init__(self) -> None:
        self.__login = Account()
        self.__ui = LoginUI()

    def run(self):
        self.__ui.inform()
        keep = True
        while keep:
            email, password = self.__ui.interact()
            result = self.__login.authenticate(email, password)
            
            if not result:
                self.__ui.print("Wrong password or email!\n", "red")
            else:
                keep = False
        


if __name__ == "__main__":
    login_page = LoginPage()
    login_page.run()