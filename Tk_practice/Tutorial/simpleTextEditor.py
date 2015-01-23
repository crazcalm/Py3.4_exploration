from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg


def generic_msg(title='Alert', text='Not ready yet.\nSorry'):
    msg.showinfo(title, text)

FILEMENU = (
    ('New', generic_msg),
    ('Open', generic_msg),
    ('Save', generic_msg),
    ('Save as', generic_msg),
    ('Close', generic_msg)
)

SENTENCE1 = "I can write things to the screen!!!"
SENTENCE2 = "This is kind of cool!!!!!!!"


class TextSection(Text):
    def __init__(self, parent, state=NORMAL):
        super().__init__(parent, state=state)
        self.parent = parent

        # Writes Text to the screen
        self.insert_text(SENTENCE1)
        self.insert_text(SENTENCE2)

        # Render to Screen
        self.pack()

    def insert_text(self, text):
        self.insert(INSERT, text)


class NavBar(Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.file_menu = None

        # Creates the File Tab
        self.create_tab("File", self.file_menu, FILEMENU)

        # displays the menus
        parent.config(menu=self)

    def create_tab(self, name, menu, options, tearoff=0):
        menu = Menu(self, tearoff=tearoff)

        # Creates the list of options
        for label, command in options:
            menu.add_command(label=label, command=command)

        # Adds this menu to the main Nav bar
        self.add_cascade(label=name, menu=menu)


class Gui(Frame):
    def __init__(self, root, width=600, height=800):
        super().__init__(root, width=width, height=height)
        self.root = root
        self.nav_bar = None
        self.text_section = None

        # Gives the Gui a Title
        self.set_title("Simple Text Editor")

        # Create Gui Parts
        self.create_nav_bar()
        self.create_text_section()

        # packs the Gui
        self.pack()

    def set_title(self, title):
        self.root.title(title)

    def create_nav_bar(self):
        self.nav_bar = NavBar(self.root)

    def create_text_section(self):
        self.text_section = TextSection(self.root)

if __name__ == '__main__':
    root = Tk()
    test = Gui(root)
    test.mainloop()