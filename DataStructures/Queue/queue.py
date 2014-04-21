"""
Queue: A queue is a collection of items where the addition of new items
        happens at one end, called the "rear," and the removal of existing
        items occurs at the other end, commonly called the "front."

This ordering principle is sometimes called FIFO (first in first out).
"""

class Queue:
    """
A basic Queue that follows the first-in-first-out principle.
    """

    def __init__(self):
        """
        Initializes the queue.
        """
        self.items = []

    def isEmpty(self):
        """
        Checks to see if the queue is empty.
        """
        return self.items == []

    def enqueue(self, item):
        """
        Inserts items to the rear of the queue.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Pops items from the front of the Queue
        """
        return self.items.pop()

    def size(self):
        """
        Returns the size of the queue
        """
        return len(self.items)
