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

#myTurtle = Turtle()
#myWin = myTurtle.getscreen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        time.sleep(0.2)
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen - 5)

def tree(branchLen, t):
    if branchLen > 5:
        time.sleep(0.2)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen - 10, t)
        t.right(20)
        t.backward(branchLen)

def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole,toPole,fromPole)

def moveDisk(fp, tp):
    print("moving disk from %s to %s\n" % (fp, tp))

if __name__ == "__main__":
    #myTurtle = Turtle()
    #myWin = myTurtle.getscreen()
    #drawSpiral(myTurtle, 100)
    #tree(80, myTurtle)
    #myWin.exitonclick()
    moveTower(3,"fromPole", "toPole", "withPole")



