"""
In tkinter, there are 3 different ways to manage the geometry of your
interface; pack, grid, and place.

Pack basics:
------------

    The pack geometry derives its name from the fact that it literally packs
widgets on the first come first serve basis in the space available in the
master frame in which the widgets are pushed.

3 types of spaces:
------------------

1. unclaimed space
2. claimed but unused space
3. claimed and used space

Common pack options:
--------------------

side: LEFT, RIGHT, TOP, BOTTOM (these decided the alignment of the widget)

fill: X, Y, BOTH, NONE (decide whether the widget can grow in size)

expand: 1/0 or YES/NO (corresponding to values respectively)

anchor: NW, N, NE, E, SE, S, SW, W, and CENTER (corresponding to cardinal
                                                    directions)

internal padding (ipadx, ipady) and external padding (padx and pady), which
    all default to a value of zero.
"""

from tkinter import *

root = Tk()
Button(root, text = "A").pack(side = LEFT, expand = YES, fill = Y)
Button(root, text = "B").pack(side = TOP, expand = YES, fill = BOTH)
Button(root, text = "C").pack(side = RIGHT, expand = YES, fill = NONE,
                                anchor = NE)
Button(root, text = "D").pack(side = LEFT, expand = NO, fill = Y)
Button(root, text = "E").pack(side = TOP, expand = NO, fill = BOTH)
Button(root, text = "F").pack(side = RIGHT, expand = NO, fill = NONE)
Button(root, text = "G").pack(side = BOTTOM, expand = YES, fill = NONE)
Button(root, text = "H").pack(side = TOP, expand = NO, fill = BOTH)
Button(root, text = "I").pack(side = RIGHT, expand = NO)
Button(root, text = "J").pack(anchor = SE)
root.mainloop()




































