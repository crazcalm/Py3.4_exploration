"""
                        Priority Queue with Binary Heaps:
                        ---------------------------------

Introduction:
------------
  A priority queue acts like a queue in that you can dequeue and item by
removing it from the front. However, in a priority queue the logical order
of items inside the queue is determined by their priority. The highest priority
items are at the front of the queue and the lowest priority items are at the
back.

  The classic way to implement a priority queue is using a data structure
called a binary heap. A binary heap will allow us to both enqueue and dequeue
items in O(logn).

  The binary heap is interesting to study because when we diagram the heap it
looks a lot like a tree, but when we implement it we only use a single list
as an internal representation.

  The binary heap has two common variations: the 'min heap,' in which the
smallest key is always at the front, and the 'max heap,' in which the largest
key is always at the front.

  In this section, we will implement the min heap.


Basic Operations List:
---------------------

  BinaryHeap(): creates a new, empty binary heap.

  insert(k): adds a new item to the heap.

  findMin(): returns the item with the minimum key value, leaving item in the heap.

  delMin(): returns the item with the minimum key value, removing the item from the list.

  isEmpty(): returns true if the heap is empty, false otherwise.
"""


