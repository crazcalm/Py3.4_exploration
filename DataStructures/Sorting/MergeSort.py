"""
                    Merge Sort:
                    -----------

Basics:
-------

    (Divide and Conquer Strategy)

    Merge sort is a recursive algorithm that continually splits a list in half.
If the list is empty or has one item, it is sorted by definition (base case).
If the list has more than one item, we split the list and recursively invoke
a merge sort on both halves. 

    Once the two halves are sorted, the fundamental operation, called a 'merge,'
is performed. Merging is the process of taking two smaller sorted lists and
combining them together into a single, sorted, new list.
"""
from BubbleSort import randomList

def mergeSort(alist):
    #print("Splitting", alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i = i+1

            else:
                alist[k] = righthalf[j]
                j = j+1
            k=k+1

        while i<len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j<len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1

    #print("Merging ", alist)
    return alist

if __name__ == "__main__":
    test = randomList(20)
    print(test, "\n")
    print(mergeSort(test))
