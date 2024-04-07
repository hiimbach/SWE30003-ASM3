from logic import Receipt
from utils.ui import UI

class ReceiptUI(UI):
    def __init__(self, receipt: Receipt) -> None:
        super().__init__("Receipt")
        self.__receipt = receipt
        
    def description(self):
        user = self.__receipt.user_info()
        name = user.name 
        total_money = self.__receipt.total_money()
        date = self.__receipt.transaction_date()
        
        self.print("All Your Healthy Food Store confirms your purchase with the following details:", "yellow")
        self.print(f"Name: {name}")
        self.print(f"Total Money Paid: {total_money}$")
        self.print(f"Transaction Time: {date}")
        self.print("\nThank you for shopping with us!", "yellow")
        
    def interact(self):
        self.get("Type anything to quit: ")