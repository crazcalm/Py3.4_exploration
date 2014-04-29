"""
                Bubble Sort:
                ------------

Basics:
-------

The buble sort makes multiple passes through a list. It compares adjacent
items and exchanges those that are out of order. Each pass through the list
places the next largest value in its proper place.


Walk Through:
-------------

If there are n items in the list, then there are n-1 pairs of items that need
to be compared on the first pass.

At the start of the second pass, the largest value is now in place. There are
n-1 items left to sort, meaning that there will be n-2 pairs.

Since each pass places the next largest value in place, the total number of
passes necessary will be n-1
"""
import pprint
import random

def randomList(num):
    """
    A quick and dirty randome list generator
    """
    stack = []
    for x in range(num):
        tempt = random.randint(0, 20)
        stack.append(tempt)
    return stack


def bubbleSort(alist):
    """
    Basic Bubble Sort
    """
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                tempt = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = tempt
    return alist

def shortBubbleSort(alist):
    """
    A version of a bubble sort that stops when exchanges cease to be made.
    """
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                tempt = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = alist[i]
    return alist


if __name__ == "__main__":
    test = randomList(20)
    print(test)
    print(bubbleSort(test))
    print(shortBubbleSort(test))
