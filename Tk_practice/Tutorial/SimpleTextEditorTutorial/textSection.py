from tkinter import *
from tkinter.ttk import *


class TextSection(Text):
    """
    This widget controls the Text box
    """
    def __init__(self, master_frame, state=NORMAL,
                 yscrollcommand=None,
                 height=80, width=100):
        super().__init__(master_frame.root, state=state,
                         yscrollcommand=yscrollcommand.set,
                         height=height, width=width)

        # Reference to root
        self.parent = master_frame.root

        # Reference to the Main GUI
        self.master = master_frame

        # Setting the Scrollbar
        self.y_scrollbar = yscrollcommand
        self.y_scrollbar.config(command=self.yview)

        # Render to Screen
        self.pack(fill=BOTH)

        # Ensures that the textbox is cleared
        self.clear_text()

    def insert_text(self, text):
        """
        Inserts text to the text box

        :param text: str
        :return: None
        """
        self.insert(INSERT, text)

    def clear_text(self):
        """
        Clears the text from the index '1.0' to the 'END' of
        the text box

        :return: None
        """
        self.delete("1.0", END)

    def get_all_text(self):
        """
        Returns all of the text within the Textbox

        :return: str
        """
        return self.get("1.0", END)