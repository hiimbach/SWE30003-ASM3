from utils.ui import UI 
from logic import Account

class RegisterUI(UI):
    def __init__(self) -> None:
        super().__init__("Register")
        self.__register = Account()    
        
    def description(self):
        self.print("Welcome to All Your Healthy Food Store!", "yellow")
        self.print("Please enter the following information to register.")
        self.print("Remember that the email should be unique. You will use this email to login.")
        self.print("Password should be at least 8 characters long.")
    
    def interact(self):
        keep = True
        while keep:
            name = self.get(text="Enter your name or press q to quit: ")

            if name.lower() == "q":
                keep = False
            else:
                keep_mail = True
                while keep_mail:
                    email = self.get(text="Enter your email or press q to quit: ")
                    # Check if email is already in use
                    keep_mail = self.__register.check_email_exist(email)
                    if keep_mail:
                        self.print("Email is already in use. Please try another email.\n", "red")

                if email.lower() == "q":
                    keep = False
                else:
                    keep_pass = True
                    while keep_pass:
                        password = self.get(text="Enter your password or press q to quit: ")
                        if password.lower() == "q":
                            keep = False
                            keep_pass = False
                        elif len(password) < 8:
                            self.print("Password should be at least 8 characters long.\n", "red")
                        else:
                            keep_pass = False

                    if password.lower() == "q":
                        keep = False
                    else:
                        phone = self.get(text="Enter your phone number or press q to quit: ")
                        
                        if phone.lower() == "q":
                            keep = False
                        else:
                            keep_age = True
                            while keep_age:
                                age = self.get(text="Enter your age or press q to quit: ")
                                if age.lower() == "q":
                                    keep = False
                                    keep_age = False
                                try:
                                    age = int(age)
                                    keep_age = False
                                except:
                                    self.print("Age should be a number.\n", "red")
                                    
                            address = self.get(text="Enter your address or press q to quit: ")
                            if address.lower() == "q":
                                keep = False
                            else:
                                return (name, email, password, phone, age, address)
                    

        return None