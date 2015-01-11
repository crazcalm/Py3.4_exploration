from tkinter import *
from tkinter import ttk

class Passwords(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Gives a title to the GUI
        master.title("Password GUI")

        # I don't know
        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.rowconfigure(0, weight=1)

        # setting up the needed Variables
        self.username = StringVar()
        self.password = StringVar()

        # Layout the GUI Labels
        ttk.Label(self.mainframe, text="Username").grid(row=1, column=0)
        ttk.Label(self.mainframe, text="Password").grid(row=2, column=0)

        # Layouts the GUI entry sections
        self.username_entry = ttk.Entry(self.mainframe, width=7,
                                        textvariable=self.username)
        self.username_entry.grid(row=1, column=1)

        self.password_entry = ttk.Entry(self.mainframe, width=7,
                                        textvariable=self.password)
        self.password_entry.grid(row=2, column=1)

        # Button
        self.button = ttk.Button(self.mainframe, text="Print",
                                 command=self.print_info)
        self.button.grid(row=3, column=1)

        # other stuff
        self.username_entry.focus()
        master.bind('<Return>', self.print_info)

        # This is needed to put all the pieces together and render it
        self.pack()
    def print_info(self, *args):
        try:
            print(args)
            username = self.username.get()
            password = self.password.get()
            print("""
            Username: {0},
            Password: {1}
            """.format(username, password))
        except ValueError:
            pass

if __name__ == "__main__":
    root = Tk()
    test = Passwords(root)
    test.mainloop()
