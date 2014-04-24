"""
Place Geometry Manager:
-----------------------

    The place geometry manager is the most rarelyused geometry manager in
Tkinter. Nevertheless, it has its uses in that it lets you precisely position
widgets within its parent frame using the X-Y coordinate system.

Options:
--------

1. Absolute positioning (specified in terms x=N, y=N)

2. Relative positioning (key options include relx, rely, relwidth, and
relheight)

3. Other commenly used options include width and anchor.

Notes:
------

    The place manager is useful in situations where you have to implement
the custom geometry managers where the widget placement is decided by the
end user.

    While the place and grid managers cannot be used in the same frame, the
place manager can be used with any other geometry manager within the same
container.
"""

from tkinter import *

root=Tk()
# Absolute positioning
Button(root, text="Absolute Position").place(x=20, y=10)
# Relative Postioning
Button(root, text="Relative Position").place(relx=0.8, rely=0.2, relwidth=0.5,
                        width=10, anchor=NE)
root.mainloop()


