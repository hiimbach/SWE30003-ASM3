import termcolor
from abc import ABC, abstractmethod

class UI(ABC):  # Abstract class
    def __init__(self) -> None:
        super().__init__()
        self.__page_name = ""
    
    def display(self):
        title = f"{'═'*30} {self.__page_name} {'═'*30}"
        self.print(title, "blue")
        print()
        
        self.description()
        print()
        self.print("═"*len(title), "blue")
        print()
        
        result = self.main()
        return result
        
        
    
    def print(self, text, color=None, tab=0):
        full_text = "   "*tab + text
        if color:
            print(termcolor.colored(full_text, color))
        else:
            print(full_text)
                        
    def get(self, text: str, tab=0):
        return input(f"{tab*'   '}> {text}")
            
    @abstractmethod           
    def description():
        pass
    
    @abstractmethod
    def main(description):
        pass
    
            
        