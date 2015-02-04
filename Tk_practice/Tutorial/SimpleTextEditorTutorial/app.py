from tkinter import *
from tkinter.ttk import *
from tkComponents import ScrollBarComponent
from constants import HEIGHT, WIDTH, SENTENCE1, SENTENCE2
from textSection import TextSection
from navBarSection import NavBar
from utilities import parse_filename


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
        self.current_file_name = None

        # Gives the Gui a Title
        self.set_title()

        # Create Gui Parts
        self.create_nav_bar()
        self.create_text_section()

        # packs the Gui
        self.pack()

        # Testing things out
        print("""height: {0},
        width: {1}""".format(self.winfo_height(), self.winfo_width()))

    def set_title(self, file_name=''):
        """
        Sets the title for the GUI

        :param title: str
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
        test = filedialog.askopenfile()
        generic_msg(text=test.name)
        print(test)
        self.text_section.clear_text()
        with open(test.name, "r") as f:
            text = f.read()
            self.text_section.insert_text(text)

        self.text_section.pack()

        # Save the name of the file
        self.current_file_name = test.name

        # Alter the GUI Title
        file_name = parse_filename(test.name)
        self.set_title(file_name=": " + file_name)

    def save_new_file(self):
        file_name = filedialog.asksaveasfilename()
        print("asksaveasfilename:", file_name)

        # Cancelling the process results in an empty string
        if file_name != "":
            with open(file_name, "w") as f:
                text = self.text_section.get_all_text()
                f.write(text)

        # Save the name of the file
        self.current_file_name = file_name

        # Alter the GUI Title
        self.set_title(file_name=": " + file_name)

    def save_existing_file(self):
        file_name = self.current_file_name

        with open(file_name, "w") as f:
            text = self.text_section.get_all_text()
            f.write(text)

if __name__ == '__main__':
    root = Tk()
    test = Gui(root)
    test.mainloop()