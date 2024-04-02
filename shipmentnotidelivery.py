from datetime import datetime, timedelta
import time

class DeliverySystem: 
    def get_orders_in_last_hour(n):
        orders_in_last_hour = []
        current_time = datetime.now()
    
        for i in range(n):
           hour_to_check = (current_time - timedelta(hours=i)).hour
           order = f"Order for hour {hour_to_check}"  # Placeholder for actual order retrieval logic
           orders_in_last_hour.append(order)
    
        return orders_in_last_hour
    

    def add_order(receipt_details, store_info): 
        print("Receipt Details: " + receipt_details)
        print("Store Info: " + store_info)
    
    receipt_details = {
    "order_id": 1,
    "products": ["Apple", "Spinach", "Quinoa"],
    "total_price": 2.42
    }

    store_info = {
    "store_name": "AYHF Store",
    "location": "123 Main St"
    }

    add_order(receipt_details, store_info)

    def notify_admin_shipment(all_order_info):
        #print("Admin notified of shipment: " + all_order_info)
        while True:
            for order_id, details in all_order_info.items():
               print(f"Notifying admin: Order ID {order_id}, Product: {details['product']}, Price: {details['price']}, Amount: {details['amount']}")
            time.sleep(3600)  # Sleep for one hour (3600 seconds)
    def notify_admin_order(receipt_details, store_info):
        print("Admin notified of order: " + receipt_details)
        print("Store: " + store_info)
        

class Shipment: 
    def all_order_info():
        order_info = {
        1: {"product": "Apple", "price": 0.99, "amount": 2},
        2: {"product": "Spinach", "price": 1.49, "amount": 3},
        3: {"product": "Quinoa", "price": 2.99, "amount": 4}
    }
    
        for order_id, details in order_info.items():
            print(f"Order ID: {order_id}")
            for key, value in details.items():
               print(f"{key}: {value}")
    all_order_info()

    #    for hour in range(24):
    #       print(f"Hour {hour}:")
    #       for order in orders:
    #           if order['hour'] == hour:
    #              print(f"Order ID: {order['id']}, Item: {order['item']}, Quantity: {order['quantity']}")

    #    orders = [
    #    {'id': 1, 'item': 'Apple', 'quantity': 3, 'hour': 8},
    #    {'id': 2, 'item': 'Banana', 'quantity': 2, 'hour': 10},
    #    {'id': 3, 'item': 'Orange', 'quantity': 1, 'hour': 12},
    # Add more orders as needed
    #    ]
    #all_order_info()

class Notification:
    def __init__(self, message):
      self.message = message

    def send_notification(self):
      print(f"Sending notification: {self.message}")  # Sending message 