"""
Deque:
------

    A deque, also known as a double ended queue, is an ordered collection of
items similar to the queue. It has two ends, a front and a rear, and the items
remain positioned in the collection.

    What makes the deque different is the unrestrictive nature of adding and
removing items. New items can be added at either the front or the rear.
Likewise, exiting items can be removed from either end.
"""

class Deque:
    """
    A basic Deque (Like a double ended queue)
    """

    def __init__(self):
        """
        Initializes Deque
        """
        self.items = []

    def isEmpty(self):
        """
        Checks to see if the deque is empty
        """
        return self.items == []

    def addFront(self, item):
        """
        Adds an item to the front
        """
        self.items.append(item)

    def addRear(self, item):
        """
        Adds an item to the rear
        """
        self.items.insert(0, item)

    def removeFront(self):
        """
        Removes an item from the front
        """
        return self.items.pop()

    def removeRear(self):
        """
        Removes an item from the rear
        """
        return self.items.pop(0)

    def size(self):
        """
        Return the size of the deque
        """
        return len(self.items)




















