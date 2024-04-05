from abc import ABC

from utils.ui.base_ui import UI

class Page(ABC):
    def __init__(self, ui: UI) -> None:
        self.__ui = ui