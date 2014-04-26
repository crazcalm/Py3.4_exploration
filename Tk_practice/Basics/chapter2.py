"""
In this chapter, we were suppose to build a text editor. However, the code is
incomplete and (in some places) incorrect.

My new game plan is to write notes on this section.
"""


"""
The below code creates a scrollbar.

Issues:
-------

Because I do not know how to set the default size of the main window, the
entire application is a 1 by 1 pixel square...

Notes:
------

1. The pattern seems to place a known section object on to root (in this case,
    it is 'Text(root)') and then configure/add what you want to the Text(root).
"""
from tkinter import *

def scrollBar():
    root = Tk()
    textpad = Text(root)
    textpad.pack(expand=YES, fill=BOTH)
    scroll = Scrollbar(textpad)
    textpad.configure(yscrollcommand = scroll.set)
    scroll.config(command=textpad.yview)
    scroll.pack(side=RIGHT, fill=Y)
    root.mainloop()

if __name__ == "__main__":
    scrollBar()
