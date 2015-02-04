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
                         height=height,
                         width=width)
        self.parent = master_frame.root
        self.master = master_frame
        self.y_scrollbar = yscrollcommand
        self.y_scrollbar.config(command=self.yview)

        # Writes Text to the screen
        self.insert_text(SENTENCE1)
        self.insert_text(SENTENCE2)

        # Render to Screen
        self.pack(fill=BOTH)

        # Testing things out
        testing = self.get("1.0", END)
        print("Text.dump:", testing)

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
        return self.get("1.0", END)