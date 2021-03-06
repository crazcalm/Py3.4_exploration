from tkinter import *
from tkinter.ttk import *


class ScrollBarComponent(Scrollbar):
    """
    This is a scrollbar component widget that can be added to other
    widgets, such as a Text widget.
    """
    def __init__(self, parent):
        super().__init__(parent)

    def set_options(self, side, fill):
        self.pack(side=side, fill=fill)
