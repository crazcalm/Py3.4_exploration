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

root = Tk()
Label(root, text="Username").grid(row=0, sticky=W)
Label(root, text="Password").grid(row=1, sticky=W)
Entry(root).grid(row=0, column=1, sticky=E)
Entry(root).grid(row=1, column=1, sticky=E)
Button(root, text="Login").grid(row=2, column=1, sticky=E)
root.mainloop()


