"""
self explanatory
"""
def sequentialSearch(alist, item):
    """
    A sequential search that returns True if it finds the searched for item
    and False otherwise.
    """
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos +1

    return found

if __name__ == "__main__":
    stack = list(range(10))
    sequentialSearch(stack, 5) == True
