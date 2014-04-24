"""
Grid Geometry Manager:
----------------------

    The central idea of the grid geometry manager is to divide the container
frame into a two-dimentional table divided into a number of rows and columns.

    Each cell in the table can be targeted to hold a widget. in this context,
a cell is an intersection of imaginary rows and columns.

    Note that in the grid method, each cell can only hold one widget. However,
widgets can be made to span multiple cells.

Options:
--------

STICKY : The sticky option decides how the widget is expanded, if its container
            is larger than the size of the widget it contains.

       - The sticky option can be specified using one or more of the N, S, E,
            and W, or NW, NE, SW, and SE options.

       - Not specifying stickiness defaults to stickiness to the center of the
            widget in the cell.
"""



from tkinter import *

def example_1():
    root = Tk()
    Label(root, text="Username").grid(row=0, sticky=W)
    Label(root, text="Password").grid(row=1, sticky=W)
    Entry(root).grid(row=0, column=1, sticky=E)
    Entry(root).grid(row=1, column=1, sticky=E)
    Button(root, text="Login").grid(row=2, column=1, sticky=E)
    root.mainloop()

def example_2():
    top = Tk()
    top.title('Find & Replace')
    Label(top, text='Find:').grid(row=0, column=0, sticky='E')
    Entry(top).grid(row=0, column=1,padx=2, pady=2, sticky='NW', columnspan=9)

    Label(top, text='Replace:').grid(row=1, column=0, sticky='E')
    Entry(top).grid(row=1, column=1, padx=2, pady=2, stick='NW', columnspan=9)

    Button(top, text="Find").grid(row=0, column=11, sticky='EW', padx=2, pady=2)
    Button(top, text="Find All").grid(row=1, column=11, sticky='EW', padx=2,
                                        pady=2)
    Button(top, text="Replace").grid(row=2, column=11, sticky='EW', padx=2,
                                        pady=2)
    Button(top, text="Replace All").grid(row=3, column=11, sticky='EW', padx=2,
                                        pady=2)

    Checkbutton(top, text="Match whole word only").grid(row=2, column=1,
                                        columnspan=3, sticky="W")
    Checkbutton(top, text="Match Case").grid(row=3, column=1,
                                        columnspan=3, sticky="W")
    Checkbutton(top, text="Wrap around").grid(row=4, column=1,
                                        columnspan=3, sticky="W")

    Label(top, text="Direction:").grid(row=2, column=4, sticky="W")
    Radiobutton(top, text="Up", value=1).grid(row=3, column=4,
                                        columnspan=2, sticky="W")
    Radiobutton(top, text="Down", value=2).grid(row=3, column=5,
                                        columnspan=2, sticky="E")

    top.mainloop()

if __name__ == "__main__":
    #example_1()
    example_2()
