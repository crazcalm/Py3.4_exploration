"""
                    Shell Sort:
                    ----------

Basics:
-------

    The shell sort, sometimes called the "diminishing increment sort," improves
on the insertion sort by breaking the original list into a number of smaller
sublists, each of which is sorted using an insertion sort.

    The unique way that these sublists are chosen is the key to the shell sort.
Instead of breaking the list into sublists of contiguous items, the shell sort
uses an increment i, sometimes called the 'gap,' to create a sublist by
choosing all items that are i items apart.

General Idea:
-------------

    You sort the sublists, and then you sort the entire list. The sorted
sublist help in reducing the total amout of passes of the shell Sort.

Big O:
------

O(n^(3/2))
"""
from BubbleSort import randomList
from InsertionSort import insertionSort

def shellSort(alist):
    """
    A basic Shell Sort
    """
    sublistcount = len(alist)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        #print("After increments of size", sublistcount,
         #       "The list is", alist ,"\n")

        sublistcount = sublistcount//2

    return insertionSort(alist)

def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = 1

        while position >= gap and \
                alist[position-gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue

    return alist

if __name__ == "__main__":
    test = randomList(20)
    print(test, "\n")
    print(shellSort(test))
