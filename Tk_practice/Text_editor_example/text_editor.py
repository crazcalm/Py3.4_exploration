from tkinter import *

"""
1. First, we will start by adding the Toplevel window, one that will
contain all other widgets using the following code
"""
root = TK()

# all our code is entered here
root.mainloop()

"""
2. In this step we add the top menu buttons to our code. See the code in
2.01.py. Menus offer a very compact way of presenting a large number
of choices to the user without cluttering the interface. Tkinter offers
two widgets to handle menus.

    - The Menubutton widget: one that is part of the menu and appears on
        the top of the application, which is always visible to the end user.

    - The Menu widget: one that show a list of choices when the user clicks
        on any menu button.

To add top-level menu buttons, you use the following command
"""

# example code
mymenu = Menu(parent, **options)
"""
For example, to add a file menu, we use the following code
"""
# Adding Menubar in the widget
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0) # File menu
root.config(menu=menubar) # this line actually displays menu

"""
Similarly, we add the Edit, View, and About menus at the top. Refer to step 2
of 2.01.py

Most of the Linux platforms tear-off menus. When tearoff is set to 1 (enabled),
the menu appearswith a dotted line above the menu options. Clicking on the
dotted line enables the user to literally tear off or seperate the menu
from the top. However, as this is not a cross-platform feature, we have
decided to disable tear-off, marking it as tearoff = 0

3. Now we will add menu items within each of the four menu buttons. As
previously mentioned, all drop-down options are to be added within the menu
instance. In our example, we add five drop-down menu choices in the File menu,
namely New, Open, Save, Save As, and Exit menus. See step of 2.02.py.

Similarly, we add the following menu choices for other menus:

    - Under Edit we have Udoe, Redo, Cut, Copy, Paste, Find All, Select All
    - Under the View we have Show Line number, Show Info Bar at Bottom,
        Highlight Current Line, and Themes.
    - Under About we have About and Help

The format for adding menu items is as follows:
"""

# example code
mymenu.add_command(label="Mylabel", accelerator="KeyBoard Shortcut",
                   compound=LEFT, image="myimage", underline=0,
                   command="callack")

menubar.add_command(label='Undo', accelerator='Ctrl + Z',
                    compound=LEFT, image="undoimage", commnad="undocallback")

"""
4. Next we will add some labels. We will add the top label, which will later
hold the shortcut buttons. We will also add a label to the left-hand side to
display the line numbers:

Having reserved the space, we can later add shortcuts icons or line numbers
keeping the label as the parent widget. Adding labels is easy, we have done in
the past. See the code in 2.02.py step 4. The code is as follows:
"""
shortcutbar = Frame(root, height=25, bg="light sea green")
shortcutbar.pack(expand=NO, fill=X)
inlabel = Label(root, width=2, bg='antique white')
inlabel.pack(side=LEFT, anchor='nw', fill=Y)

"""
We have applied a colorful background to these two labels for now to
differentiate it from the body of the Toplevel window.

5. Lastly, let's add the Text widget and Scrollbar widget to out code.
Refer to the stop 5 of the code 2.02.py
"""
textpad = Text(root)
textpad.pack(expand=YES, fill=BOTH)
scroll = Scrollbar(textpad)
textpad.configure(yscrollcommand=scroll.set)
scroll.config(command=textpad.yview)
scroll.pack(side=RIGHT, fill=Y)

"""
The code is similar to all other code that we have used so far to instantiate
widgets. Notice, however, that the scrollbar is configured to yview of the
Text widget and the Text widget is configured to connect to the Scrollbar
widget. This way, we cross connected both the widgets to each other.

Now when you go down the Text widget, the scrollbar reacts to it.
Alternatively, when you pull the scrollbar, the Text widget reacts in return.

Some new menu-specific options introduced here are as follows:

    - accelerator: This option is used to specify a string, typically the
keyboard shortcut, which can be used to invoke the menu. The string specified
as the accelerator appears next to the text of the menu item. Please note
that this does not automatically create bindings for the keyboard shortcut.
We will have to menually set them up, as we will see later.

    - compound: Specifying a compound option to the menu item lets you add
images beside the common text label of the menu. A specification such as
Compound=LEFT, label= 'mytext', image='myimage' means that the menu
item has a compound label comprising of a text label and an image, where
the image is to be placed on the left-han side of the text. The images we
use here are stored and referenced from a seperate folder called icons.

    - underline: The underline option lets you specify the index of a character
in the menu text to be underlined. The indexing starts at 0, which means
that specifying underline=1 underlines the second character of the text.
Besides underlining, Tkinter also uses it to define the default bindings
for keyboard traversal of menus. This means that we can select the menu
either with the mouse pointer, or with the Alt + <character_at_the_underline
_index> shortcut.

Therefore, to add the New menu item within the File menu, we use the
following code:
"""

# example code
filemenu.add_command(label="New", accelerator='Ctrl+N', compound=LEFT,
                     image='newIcon', underline=0, command='new_file')

"""
Similarly, we add menu choices for the Edit menu.

Other than the normal menu type that we implement for the New and Edit menus,
Tkinter offers three more variables of the menu:

    - The Checkbutton menu: This menu lets you make a yes/no choice by
    checking/unchecking the menu.

    - The Radiobutton menu: This menu lets you choose one from among many
    different options.

    - The Cascade menu: This menu only opens up to show another list of
    choices.

Our View menu demonstrates all these three types of menus as shown in
the following screenshot:

[screenshot]

The first three choices under the View menu let the user select whether or
not they want a certain thing to happen. The user can check/uncheck options
against these menus and are examples of the Checkbutton menu.

The fourth menu choice under View reads as Themes. Hovering over this menu
opens another list of choices. This is an example of a Cascade menu
as it only serves the purpose of opening up another list of choices.

Within the Cascade menu, you are presented with a list of choices for
your editor theme. You can, however, select only one of the themes.
Selecting one theme unselects any previous selection. This is an example
of the Radiobutton menu.

An example format for adding these three types of menu is as follows:
"""
viewmenu.add_checkbutton(label="Show Line Number", variable='showln')
viewmenu.add_cascade(label='Themes', menu=themesmenu)

themesmenu.add_radiobutton(label="Default white", variable=theme)

"""
Now that we need to track whether or not a selection has been made, we
track it by adding a variable that can be BooleanVar(), IntVar(), Stringvar()
as we discussed in Project 1, Meet Tkinter.

For a complete list of configuration options for them Menubutton and Menu
widgets, refer to The basic methods section in Appendix B, Quick Reference
Sheets.
"""
