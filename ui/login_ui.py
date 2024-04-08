from ui import UI

class LoginUI(UI):
    def __init__(self) -> None:
        super().__init__("Login")
        
    def description(self):
        print("Enter credentials to login")

    def interact(self):
        keep = True
        while keep:
            email = self.get(text="Enter your email or press q to quit: ")
                
            if email.lower() == "q":
                keep = False

            else:
                password = self.get(text="Enter password or press q to quit: ")

                if password.lower() == "q":
                    keep = False

                else:
                    accountCredentials = (email, password)
                    return accountCredentials

        return (None, None)
    
    def announceSuccessful(self):
        print("You have logged in successfully")

    def announceFailure(self, message):
        print("Registration unsuccessful: " + message)