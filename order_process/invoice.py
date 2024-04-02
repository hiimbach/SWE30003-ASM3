from order_process.order import Order

class Invoice:
    def __init__(self, order: Order, filename: str) -> None:
        self.order = order
        self.filename = filename

    def generate_invoice(self):
        print("\nOrder Details:")
        print("Customer: ", self.user_info.uname)
        print("Customer's Email: ", self.user_info.email)
        print("Customer's Phone Number: ", self.user_info.phone_num)
        print("Item: ", self.product_container.name)
        print("Amount: ", self.product_container.amount)
        print("Price per item: $ ", self.product_container.price)
        print("Total amount: $ ", self.total_amount())


