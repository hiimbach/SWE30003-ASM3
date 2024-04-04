from features.info import Info

class UserInfo(Info):
    name: None
    contactNumber: None
    address: None
    creditCardNumber: None

    def __init__(self, name, contactNumber, address, creditCardNumber) -> None:
        self.name = name
        self.contactNumber = contactNumber
        self.address = address
        self.creditCardNumber = creditCardNumber

    def setAddress(self, newAddress):
        self.address = newAddress

    def setContactNumber(self, newCreditCardNumber):
        self.contactNumber = newCreditCardNumber

    def getAddress(self):
        return self.address

    def getContactNumber(self):
        return self.contactNumber