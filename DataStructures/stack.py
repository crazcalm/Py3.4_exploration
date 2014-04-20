"""
Stack: is an ordered collection of items where the addition of new items
        where the addition of new items and the removal of existing items
        always takes place at the same end.

A stack is otherwise known as LIFO (last in first out).
"""

class Stack:
    def __init__(self):
        """Initializes the Stack"""
        self.items = []

    def isEmpty(self):
        """Checks to see if the Stack is empty"""
        return self.items == []

    def push(self, item):
        """Adds an element to the stack"""
        self.items.append(item)

    def pop(self):
        """Removes the last item from the stack"""
        return self.items.pop()

    def peek(self):
        """Returns the item that is at the top of the Stack"""
        return self.items[len(self.items) - 1]

    def size(self):
        """Returns the length of the Stack"""
        return len(self.items)


