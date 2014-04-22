"""
I will learn tkinter!
"""

from tkinter import *
root = Tk()
mylabel = Label(root, text="I am a label widget")
mybutton = Button(root, text="I am a button")
mylabel.pack()
mybutton.pack()
root.mainloop()

"""
Notes:

Every tkiner gui needs a root, which is going to be your main window.
We create other widgets and then placed them on the main window (root).

In this example, we creates two widgets (Label and Button) and placed them
on the main window.
"""
