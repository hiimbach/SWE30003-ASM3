from abc import ABC, abstractmethod, abstractproperty

class Info(ABC):

    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def contactNumber(self):
        pass

    @abstractmethod
    def modifyName(self):
        pass

    @abstractmethod
    def modifyContactNumber(self):
        pass   

    def setName(self, newName):
        self.name = newName

    def setContactNumber(self, newContactNumber):
        self.contactNumber = newContactNumber

    def getName(self):
        return self.name
    
    def getContactNumber(self):
        return self.contactNumber