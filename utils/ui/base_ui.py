import termcolor
from typing import List, Union
from abc import ABC, abstractmethod

class UI(ABC):  # Abstract class
    def __init__(self, page_name="") -> None:
        super().__init__()
        self.__page_name = page_name
    
    def inform(self):
        title = f"{'═'*33} {self.__page_name} {'═'*33}"
        self.print(title, "blue")
        print()
        
        self.description()
        print()
        self.print("═"*len(title), "blue")
        print()
    
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
    def interact(description):
        pass
    
    def get_range(self, range_: Union[int, List], text):
        keep = True
        while keep:
            option = self.get(text=text)
                
            if option.lower() == "q":
                keep = False
            else:
                try:
                    option = int(option)
                except ValueError:
                    self.print("Invalid option. Please try again.\n", color="red")
                    continue
                if isinstance(range_, int):
                    number_range = range(1,range_+1)
                else:
                    number_range = range(range_[0], range_[1])
                if option in number_range:
                    return option
                    
                else:
                    self.print("Invalid option. Please try again.\n", color="red")
                    
        return None
