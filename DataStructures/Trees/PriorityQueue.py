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

  size(): returns the number of items in the heap.

  buildHeap(list): builds a new heap from a list of keys.


The Structure Property:
-----------------------

  In order to make our heap work effeciently, we will take advantage of the
logarithmic nature of the tree to represent our heap.

  In order to guarantee logarithmic performance, we must keep our tree balanced.
A balanced binary tree has roughly the same number of nodes in the left and right
subtrees of the root.

  In our heap implemention we keep the tree balanced by creating a 'complete
binary tree.'

  A complete binary tree is a tree in which each level has all of its nodes.
The exception to this is the bottom of the tree, which we fill in from left to
right.


Interesting Property:
---------------------

  Another interesting property of a complete tree is that we can represent it
using a single list. We do not need to use nodes and references or even lists
of lists.

  Because the tree is complete, the left child of the parent (at position p) is
is the node that is found a position 2p in the list. Similarly, the right child
of the parent is at position 2p+1 in the list.


The Heap Order Property:
------------------------

  The 'heap order property' is as follows: In a heap, for every node x with
parent p, the key in p is smaller than or equal to the key in x.


Heap Operations:
----------------

  We will begin our implemention of a binary heap with the constructor.
Since the entire binary heap can be represented by a single list, all the constructor
will do is initialize the list and an attribute currentSize to keep track of the
current size of the heap.

  You will notice that an empty binary heap has a single zero as the first element
of heapList and that this zero is not used, but is there so that a simple
integer can be used in later methods.
"""


