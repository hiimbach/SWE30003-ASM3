import sys 
sys.path.append('.')
from utils.ui import ReceiptUI
from pages import Page
from logic import Receipt

class ReceiptPage(Page):
    def __init__(self, invoice_id: int) -> None:
        self.__receipt = Receipt(invoice_id)
        self.__receipt_ui = ReceiptUI(self.__receipt)
        
    def run(self): 
        self.__receipt_ui.inform()
        self.__receipt_ui.interact()
        
    
if __name__ == "__main__":
    receipt_page = ReceiptPage(1)
    receipt_page.run()