"""
Binary Search:
--------------

A binary search will start by examining the middle item. If that item is the
one we are searching for, we are done. If it is not the correct item, we can
use the ordered nature of the list to eliminate half of the remaining items.

If the item we are searching for is greater than the middle item, we know that
the entire lower half of the list as well as the middle can be eliminated from
further consideration.

We can then repeat the process with the upper half. Start at the middle item
and compare it against what we are looking for. Again, we either find it or
split the list in half, therefore eliminating another large part of
our possible search.

Big O:
------
O(logn)

or n/(2^i), where i is the number of comparisions. Solving for i gives use
the above big O.
"""


