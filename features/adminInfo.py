from features.info import Info

class UserInfo(Info):
    name: None
    contactNumber: None

    def __init__(self, name, contactNumber, address, creditCardNumber) -> None:
        self.name = name
        self.contactNumber = contactNumber
        self.address = address
        self.creditCardNumber = creditCardNumber
