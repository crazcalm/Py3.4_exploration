"""
                Selection Sort:
                ---------------

Basics:
-------

    The selections sort improves on the bubble sort by making only one exchange
for every pass through the list. In order to do this, a selection sort looks
for the largest value as it makes a pass and, after completing the pass, places
it in the proper location.

Logic:
------

    The same as the Bubble Sort (more of less).

Big O:
------

O(n^2)
"""
from BubbleSort import randomList


def selectionSort(alist):
    """
    A basic selection Sort
    """
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        tempt = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = tempt

    return alist

if __name__ == "__main__":
    test = randomList(20)
    print(test)
    print(selectionSort(test))
