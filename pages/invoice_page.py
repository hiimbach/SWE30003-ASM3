import sys 
import os
sys.path.append('.')

from logic import Invoice, Inventory, Cart
from pages import ReceiptPage, Page
from ui import InvoiceUI

class InvoicePage(Page):
    def __init__(self) -> None:
        self.__invoice_ui = InvoiceUI()
        self.__inventory = Inventory()  
        self.__invoice = Invoice()
        self.__cart = Cart()
        
    def run(self):
        self.__cart.update()
        self.__invoice_ui.inform()
        option = self.__invoice_ui.interact()
        
        if option == None:
            return
        else:
            if option == 1:
                # Confirm invoice
                cart_info = self.__invoice.cart_info().current()
                invoice_id = self.__invoice.save_invoice()
                for item in cart_info:
                    product_name = item['Product']
                    product = self.__inventory.from_product_name(product_name)
                    amount = item['Amount']
                    self.__inventory.reduce_amount(product, amount)
                    self.__cart.modify_product(product, -amount)
                
                
                # Move to receipt 
                receipt_page = ReceiptPage(invoice_id)
                receipt_page.run()
                
            else:
                # Cancel invoice
                return 
        
        
if __name__ == "__main__":
    invoice_page = InvoicePage()
    invoice_page.run()
    