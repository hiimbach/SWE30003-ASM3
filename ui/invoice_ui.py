from ui import UI, CartUI
from logic import Invoice, UserManagement


class InvoiceUI(UI):
    def __init__(self) -> None:
        super().__init__("Invoice Details")
        self.__invoice = Invoice()
        
        self.__user_info = self.__invoice.user_info()
        self.__cart_ui = CartUI()
        
    def description(self):
        self.print("Bill To:", "yellow")
        self.print(f"User: {self.__user_info.name}")
        self.print(f"Address: {self.__user_info.address}")
        self.print(f"Phone: {self.__user_info.phone}")
        self.print(f"Email: {self.__user_info.email}")
        self.print("")
        self.print("Invoice Details:", "yellow")
        self.__cart_ui.description()
        
    def interact(self):
        self.print("1. Confirm Invoice and Pay")
        self.print("2. Cancel Invoice")
        option = self.get_range(range_=2,
                                text="Choose an option based on the number, or type Q to quit: ")
        return option
            
            
             