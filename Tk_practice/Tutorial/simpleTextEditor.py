from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
from tkinter import filedialog


# TODO Move untilty function to its own file
def generic_msg(title='Alert', text='Not ready yet.\nSorry'):
    """
    Shows the user a msg

    :param title: str
    :param text: str
    :return: None
    """
    msg.showinfo(title, text)

# TODO Move constants to its own file
SENTENCE1 = "I can write things to the screen!!!"
SENTENCE2 = "This is kind of cool!!!!!!!"


# TODO Move each class to its own file.
class TextSection(Text):
    """
    This widget controls the Text box
    """
    def __init__(self, master_frame, state=NORMAL):
        super().__init__(master_frame.root, state=state)
        self.parent = master_frame.root
        self.master = master_frame

        # Writes Text to the screen
        self.insert_text(SENTENCE1)
        self.insert_text(SENTENCE2)

        # Render to Screen
        self.pack()

    def insert_text(self, text):
        """
        Inserts text to the text box

        :param text: str
        :return: None
        """
        self.insert(INSERT, text)

    def clear_text(self):
        """
        Clears the text from the text box

        :return: None
        """
        pass


class NavBar(Menu):
    """
    This Widget controls the nav bar options and selection
    """
    def __init__(self, master_frame):
        super().__init__(master_frame.root)
        self.parent = master_frame.root
        self.master = master_frame
        self.file_menu = None

        # Creates the File Tab
        self.create_tab("File", self.file_menu, self.get_file_menu_data())

        # displays the menus
        master_frame.root.config(menu=self)

    def create_tab(self, name, menu, options, tearoff=0):
        """
        Creates the tab for the Nav Bar and fills it with options

        :param name: str - name of the tab
        :param menu: property - A reference link between the class and the
                     menu within the tab
        :param options: iterable of two item tuples (label, command)
        :param tearoff: int - sets the value for the tearoff
        :return: None
        """
        menu = Menu(self, tearoff=tearoff)

        # Creates the list of options
        for label, command in options:
            menu.add_command(label=label, command=command)

        # Adds this menu to the main Nav bar
        self.add_cascade(label=name, menu=menu)

    def get_file_menu_data(self):
        return(
            ('Open', self.master.open_file),
            ('Save', generic_msg),
            ('Save as', generic_msg),
            ('Close', self.close),
        )

    def close(self):
        self.parent.quit()

class Gui(Frame):
    """
    This widget is the main frame of the program. The parent frame.
    """
    def __init__(self, root, width=600, height=800):
        """
        Setting the defaults for the frame

        :param root: Tk() object
        :param width: int - set default width
        :param height: int - set default height
        :return: None
        """
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
        """
        Sets the title for the GUI

        :param title: str
        :return: None
        """
        self.root.title(title)

    def create_nav_bar(self):
        """
        Creates an instance of the NavBar class and associates it with
        this class.

        :return: None
        """
        self.nav_bar = NavBar(self)

    def create_text_section(self):
        """
        Creates an instance of the TextSection class and associates it with
        this class.

        :return: None
        """
        self.text_section = TextSection(self)

    def open_file(self):
        test = filedialog.askopenfile()
        generic_msg(text=test.name)
        print(test)

if __name__ == '__main__':
    root = Tk()
    test = Gui(root)
    test.mainloop()