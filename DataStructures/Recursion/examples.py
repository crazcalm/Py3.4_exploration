"""
Recursion:
----------

    Recursion is a method of solving problems that invloves breaking
problems down into smaller and smaller subproblems until you get to a small
enough problem that it can solves trivially.

The Three Laws of Recursion:

1. A recursive algorithm must have a base case.

2. A recursive algorithm must change its state and move towards the base case.

3. A recursive algorithm must call itself, recursively.
"""

from turtle import *
import time

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

def toStr(n, base):
    convertString = "0123456789ABCDEF"

    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

myTurtle = Turtle()
myWin = myTurtle.getscreen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        time.sleep(0.2)
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen - 5)

if __name__ == "__main__":
    myTurtle = Turtle()
    myWin = myTurtle.getscreen()
    drawSpiral(myTurtle, 100)
    myWin.exitonclick()
