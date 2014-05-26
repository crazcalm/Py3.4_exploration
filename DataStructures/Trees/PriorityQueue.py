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


Insert method:
--------------

  The next method we will implement in 'insert.'

  The easiest, and most efficient, way to add an item to a list is to simply
append the item to the end of the list. The good news about appending is that
it guarantees that we will maintain the complete tree property.

  The bad news is that we will very likely violate the heap structure property.
However, it is possible to write a method that will allow us to regain the heap
structure property by comparing the newly added items with its parent.

  If the newly added item is less than its parent, then we can swap the item
with its parent.

  Notice that when we percolate an item up, we are restoring the heap property
between the newly added item and the parent. We are also perserving the heap
property for any siblings.


delMin method notes:
--------------------

  Since the heap property requires that the root of the tree be the smallest
item in the tree, finding the minimum item is easy. The hard part of delMin
is restoring full compliance with the heap structure and heap order properties
after the root has been removed.

  We can restore our heap in two steps.

  1. We will restore the root item by taking the last item in the list and moving
    it to the root position.

  2. We will restore the heap order property by pushng the new root node down
    the tree to its proper position.

  In order to maintain the heap order property, all we need to do is swap the
root with its smallest child less than the root. After the initial swap, we may
repeat the swapping process with a node and its children until the node is swapped
into a position on the tree where it is already less than both children.

  The code for percolating a node down the tree is found in the 'percDown' and
'minChild' methods.


buildHeap method:
-----------------

  To finish our discussion of binary heaps, we will look at a method to build
an entire heap from a list of keys.

  If we start with an entire list then we can build the whole heap in O(n)
operations.

  We will start from the middle of the list. Although we start out in the middle
of the tree and work our way back towards the root, the percDown method enusres that
the largest child is always down the tree. Beacuse it is a complete binary tree,
any nodes past the halfway point will be leaves and therefore have no children.
"""

class PriorityQueue:
    """
    A priority queue acts like a queue in that you can dequeue and item by
    removing it from the front. However, in a priority queue the logical order
    of items inside the queue is determined by their priority. The highest priority
    items are at the front of the queue and the lowest priority items are at the
    back.
    """

    def __init__(self):
        """
        You will notice that an empty binary heap has a single zero as the first element
        of heapList and that this zero is not used, but is there so that a simple
        integer can be used in later methods.
        """
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        """
        Compares the newly inserted item with its parent. If the item is less
        than its parents, then they will be switched.
        """
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        """
        Inserts a new item to the binary heap
        """
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        """
        Moves the root of the binary heap (or subtree of the heap) down to its
        proper place in the tree.
        """
        while(i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        """
        Returns the index of the min Child
        """
        if i * 2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        """
        Returns the smallest item in the Binary Heap
        """
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        """
        Builds a Binary Heap from a list
        """
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i>0):
            self.percDown(i)
            i = i - 1

    def isEmpty(self):
        return self.currentSize == 0

if __name__ == "__main__":
    test = [5,7,3,11]
    test2 = [9,6,5,2,3]

    bh = BinaryHeap()
    for x in test:
        bh.insert(x)

    while not bh.isEmpty():
        print(bh.delMin())

