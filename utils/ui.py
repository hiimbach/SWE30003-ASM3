import termcolor
from abc import ABC, abstractmethod

class UI():
    
    @abstractmethod
    def show(self, text, color=None):
        pass
    
    def print(self, text, color=None):
        if color:
            print(termcolor.colored(text, color))
        else:
            print(text)
            
            
