class Shipment:
  def __init__(self, order_id, product, destination):
    self.order_id = order_id
    self.product = product
    self.destination = destination
    self.status = "Created"  # Track shipment status

class DeliverySystem:
  def __init__(self, query_db):
    self.query_db = query_db  # Dependency injection for database access

  def process_delivery(self, order):
    # Find the nearest store
    store_info = self.find_nearest_store(order.receipt_details)

    # Create shipment object
    shipment = Shipment(order.receipt_details["order_id"], order.receipt_details["product"], order.receipt_details["destination"])

    # Add the order to the store
    self.add_order(shipment, store_info)

    # Notify the admin about the order
    self.notify_admin_order(shipment)

  def find_nearest_store(self, receipt_details):
    # Replace this with your logic to find the nearest store
    store_info = self.query_db.get_nearest_store(receipt_details["destination"])
    return store_info

  def add_order(self, shipment, store_info):
    # Logic to add the order to the store (e.g., update database)
    self.query_db.add_order_to_store(shipment.order_id, store_info["store_id"])
    shipment.status = "In Progress"  # Update shipment status

  def notify_admin_order(self, shipment):
    # Logic to send notification (e.g., email, SMS)
    notification = Notification(f"New order: {shipment.order_id}")
    notification.send_notification()
    shipment.status = "Notification Sent"  # Update shipment status

class Notification:
  def __init__(self, message):
    self.message = message

  def send_notification(self):
    # Replace this with your logic to send notification
    print(f"Sending notification: {self.message}")  # Placeholder
