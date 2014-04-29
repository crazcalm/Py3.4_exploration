"""
                Insertion Sort:
                ---------------

Basics:
-------

    The insertion sort, although still O(n^2), works in a slightly different
way. It always maintains a sorted sublist in the lower positions of the list.
Each new Item is then "inserted" back into the previous sublist such that the
sorted sublist is one item larger.

Logic:
------

    We begin by assuming that a list with one item (position 0) is already
sorted. On each pass, one for each item 1 through n-1, the current item is
checked against those in the already sorted sublist.

    As we look back into th already sorted sublist, we shift those items that
are greater to the right. When we reach a smaller item or the end of the
sublist, the current item can be inserted.

Big O:
------

O(n^2)
"""
from BubbleSort import randomList

def insertionSort(alist):
    """
    A basic insertion sort
    """
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position -1] >currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

    return alist

if __name__ == "__main__":
    test = randomList(20)
    print(test)
    print(insertionSort(test))
