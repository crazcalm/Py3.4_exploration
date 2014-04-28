"""
self explanatory
"""

def orderedSequentialSearch(alist, item):
    """
    This is a sequential search that assumes that the list is sorted
    """
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found

if __name__=="__main__":
    stack = list(range(20))
    print(orderedSequentialSearch(stack, 15))
