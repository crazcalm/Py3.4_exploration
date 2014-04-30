"""
                    Quick Sort:
                    -----------

Basics:
-------

    The quick sort uses divide and conquer to gain the same advantages as the
merge sort, while not using additional storage.

    As a trade-off, however, it is possible that the list may not be divided
in half. When this happens, the performance is diminished.

Pivot Value:
------------

    A quick sort first selects a value, which is called the 'pivot value.'
The role of the pivot value is to assist with the splitting the list. The
actual position where the pivot value belongs in the final sorted list,
commonly called the 'split point,' wil be used to divide the list for
subsequent calls to the quick sort.

Partition:
----------

    The partition process will happen next. It will find the split point and at
the same time move other items to the appropiate side of the list, either less
than or greater than the pivot value.

Partitioning Logic:
-------------------

    Partitioning begins by locating two position markers--let's call them
leftmark and rightmark--at the beginning and end of the remaining items in
the list.

    The goal of the partition process is to move items that are on the wrong
side with respect to the pivot value while also converging on the split point.

1. We begin by incrementing leftmark unitl we locate a value that is greater
than the pivot value.

2. We then decrement rightmark until we find a value that is less than the
pivot value.

- At this point we have discovered two items that are out of place with
respect to the eventual split point.

3. Now we can exchange these two items and then repeat the process again
(see steps 1 and 2).

4. At the point where rightmark becomes less than leftmark, we stop. The
position of rightmark is now the split point ("pivot point" is now in place).

- All of the items to the left of the split point are less than the pivot value,
and all the items to the right of the split point are greater then the pivot
value.

5. The list can now be divided at the split point and the quick sort can be
invoked recursively on the two halves.

Big O:
------

If the split occurs in the middle of the list, then O(nlogn).

Else, O(n^2)
"""





























