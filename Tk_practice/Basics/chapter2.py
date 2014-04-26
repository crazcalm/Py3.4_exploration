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

"""
                    Universal Widget Methods:
                    -------------------------

Intro:
------

Tkinter's Text widget comes with some handy built-in functionality to handle
common text-related functions. 

The documentation of Tcl/Tk 'universal widget methods' tells us that we can
trigger events without any external stimulus using the following command:

-----> textpad.event_generate("<<Cut>>")

Below is a code snippet of how you would use it:

-----------------------------------------------------------------------------------------------------------------------
-    def cut():                                                                                                       -
-        textpad.event_generate("<<Cut>>"                                                                             -
-        # Then define a command callback from our exiting cut menu like                                              -
-                                                                                                                     -
-    editmenu.add_command(label="Cut", compound=LEFT, image=cuticon, accelerator="Ctrl+x", command=cut))              -
-                                                                                                                     -
-----------------------------------------------------------------------------------------------------------------------


                    Text Widget:
                    ------------

Intro:
------

The Text widget offers us the ability to manipulate its content using
index, tags, and mark, which lets us target a position or placce within the
text area for manipulation.

Index:
------

Indexing helps you target a particular place within a text.

Index Formats:
-------------

x.y         : The yth character on line x
@x.y        : the character that covers the x.y coordinate within the text's window.
end         : The end of the text.
mark        : The character after a named mark.
tag.first   : The first character in the text that has been tagged with a given tag.
tag.last    : The last character in the text that has been tagged with a given tag.
window.name : The position of the embedded window whose name is widowname.
imagename   : The position of the embedded image whose name is imageName.
INSERT      : The posistion o
CURRENT     :


selection   : This corresponds to the current selection. The constants SEL_FIRST,
(SEL_FIRST, : and SEL_LAST refer to the start position and the end position in the
SEL_LAST)   : selection. Tkinter raises a TclError exception if there is no selection







"""

if __name__ == "__main__":
    scrollBar()




























