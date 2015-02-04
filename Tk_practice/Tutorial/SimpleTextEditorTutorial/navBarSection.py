from tkinter import *
from tkinter.ttk import *


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
            ('New', self.master.new_file),
            ('Open', self.master.open_file),
            ('Save', self.master.save_existing_file),
            ('Save as', self.master.save_new_file),
            ('Close', self.close),
        )

    def close(self):
        self.parent.quit()