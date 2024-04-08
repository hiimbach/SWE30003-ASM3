from abc import ABC, abstractmethod

from ui.base_ui import UI

class Page(ABC):
    '''
    THIS IS AN INTERFACE. PYTHON DOES NOT HAVE A NATIVE INTERFACE IMPLEMENTATION.
    '''
    def __init__(self) -> None:
        pass
        
    @abstractmethod
    def run(self):
        pass