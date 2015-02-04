from tkinter import *
from tkinter.ttk import *


class ScrollBarComponent(Scrollbar):
    def __init__(self, parent):
        super().__init__(parent)

    def set_options(self, side, fill):
        self.pack(side=side, fill=fill)
