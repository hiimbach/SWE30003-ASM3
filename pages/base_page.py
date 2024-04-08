from abc import ABC, abstractmethod

from ui.base_ui import UI

class Page(ABC):
    def __init__(self, ui: UI) -> None:
        self.__ui = ui
        
    @abstractmethod
    def run(self):
        pass