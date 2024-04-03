from order_process.order import Order

class Invoice:
    def __init__(self, order: Order, invoice_filename: str) -> None:
        self.order = order
        self.invoice_filename = invoice_filename

    def generate_invoice(self):
        print("Invoice")
        print("Customer: {}".format(self.order.user_info.uname))
        print("Email: {}".format(self.order.user_info.email))
        print("Phone Number: {}".format(self.order.user_info.phone_num))
        print("Item: {}".format(self.order.product_container.name))
        print("Amount: {}".format(self.order.product_container.amount))
        print("Price per item: ${}".format(self.order.product_container.price))
        print("Total amount: ${}".format(self.order.total_amount()))
        
        with open(self.invoice_filename, 'w') as file:
            file.write("Invoice\n")
            file.write("Customer: {}\n".format(self.user_info.uname))
            file.write("Email: {}\n".format(self.user_info.email))
            file.write("Phone Number: {}\n".format(self.user_info.phone_num))
            file.write("Item: {}\n".format(self.product_container.name))
            file.write("Amount: {}\n".format(self.product_container.amount))
            file.write("Price per item: ${}\n".format(self.product_container.price))
            file.write("Total amount: ${}\n".format(self.total_amount()))

    
