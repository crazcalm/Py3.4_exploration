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
