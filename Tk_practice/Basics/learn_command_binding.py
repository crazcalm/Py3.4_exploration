"""
Command Binding:
----------------


Introduction:
-------------

The simpliest way to add functionality to a button is called 'command
binding', whereby the callback function is mentioned in the form of
'command = some_callback' in the widget options.

EX:
    def my_callback():
        #do someting
        Button(root, text="Click", command = my_callback)

Note that my_callback is called without parentheses () from within the
widget command option. This is because when the callback functions are set,
it is necessary to pass a reference to a function rather than actually calling
it.


Passing Arguments to the Callback:
----------------------------------

If the callback needs to take some arguments, we can use the "lambda" function
as shown in the following snippet.

EX:
    def my_callback(somearg):
        # Do something with argument
        Button(root, text="Click", callback=lambda arg: my_callback(somearg))


Notes:
------

1. The format for using lambda is "lambda arg: Do something with arg in a
single line."

EX:
    lambda x: return x^2

2. Many other widgets do not provide any equivalent command binding option.

3. The command button binds by default to the left mouse click and the Space
bar. It does not bind to the return key.

    - You CAN NOT CHANGE  this binding of the command function.


Event Binding:
--------------

Tkinter provides an alternative form of event binding mechanism called "bind()"
to let you deal with different events. 

EX:
    widget.bind(event, handler)
"""

from tkinter import *

root = Tk()
Label(root, text="Click at different\nlocations in the frame below").pack()
def mycallback(event):
    # Prints event's attributes (all of them)
    print (dir(event))
    print ("You clicked at", event.x, event.y)

myFrame = Frame(root, bg="khaki", width=130, height=80)
myFrame.bind("<Button-1>", mycallback)
myFrame.pack()
root.mainloop()

