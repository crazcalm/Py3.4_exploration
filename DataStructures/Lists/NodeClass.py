"""
                The Node Class
                --------------

  The basic building block for the linked list implementation is the node.
Each node object must hold at least two pieces of information. First, the node
must contain the list item itself. We will call this the data field of the node.
In addition, each node must hold a reference to the next node.
"""

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

"""
The Unordered List Class:
-------------------------

  The unordered list will be built from a collection of nodes, each linked to
the next by explicit references. As long as we know where to find the first
node, each item after that can be found by successively following the next
links. With this in mind, the UnorderedList class must maintain a reference to
the first node. Note that each list object will maintain a single reference to
the head of the list.
"""

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        fount = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
