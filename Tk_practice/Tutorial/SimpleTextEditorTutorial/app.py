from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkComponents import ScrollBarComponent
from constants import HEIGHT, WIDTH
from textSection import TextSection
from navBarSection import NavBar
from utilities import parse_filename, generic_msg


class Gui(Frame):
    """
    This widget is the main frame of the program. The parent frame.
    """
    def __init__(self, root, width=WIDTH, height=HEIGHT):
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

        # Properties
        self.current_file_path = None

        # Gives the Gui a Title
        self.set_title()

        # Create Gui Parts
        self.create_nav_bar()
        self.create_text_section()

        # packs the Gui
        self.pack()

    def set_title(self, file_name=''):
        """
        Sets the title for the GUI

        :param file_name: str
        :return: None
        """
        title = "Simple Text Editor" + file_name
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
        y_scrollbar = ScrollBarComponent(self.root)
        y_scrollbar.set_options(RIGHT, Y)
        self.text_section = TextSection(self, yscrollcommand=y_scrollbar)

    def open_file(self):
        file_path = filedialog.askopenfile()

        # User selects a file
        if file_path:
            self.text_section.clear_text()
            with open(file_path.name, "r") as f:
                text = f.read()
                self.text_section.insert_text(text)

            self.text_section.pack()

            # Save the name of the file
            self.current_file_path = file_path.name

            # Alter the GUI Title
            file_name = parse_filename(file_path.name)
            self.set_title(file_name=": " + file_name)

        # User cancels the process
        else:
            pass

    def save_new_file(self):
        file_path = filedialog.asksaveasfilename()

        # Cancelling the process results in an empty string
        if file_path:
            with open(file_path, "w") as f:
                text = self.text_section.get_all_text()
                f.write(text)

            # Save the name of the file
            self.current_file_path = file_path

            # Alter the GUI Title
            file_name = parse_filename(file_path)
            self.set_title(file_name=": " + file_name)

    def save_existing_file(self):
        file_path = self.current_file_path

        if file_path:
            with open(file_path, "w") as f:
                text = self.text_section.get_all_text()
                f.write(text)

        else:
            generic_msg(text="Cannot Save this file. Try Save As")

    def new_file(self):
        self.current_file_path = None
        self.text_section.clear_text()
        self.set_title()

if __name__ == '__main__':
    root = Tk()
    test = Gui(root)
    test.mainloop()