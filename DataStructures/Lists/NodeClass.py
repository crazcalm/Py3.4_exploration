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

  The head of the list refers to the first node which contains the first item
of the list. In turn, that node holds a reference to the next node (the next
item) and so on. It is very important to note that the list class itself does
not contain any node objects. Instead it contains a single reference to only the first node in the linked structure.

  The isEmpty method simply checks to see if the head of the list is a reference
to None. The result of the boolean expression self.head==None will only be
true if there are no nodes in the linked list.

  So, how do we get items into our list? We need to implement the add method.
However, before we can do that, we need to address the important question of
where in the linked list to place the new item. Since this list is unordered,
the specific location of the new item with respect to the other items already
in the list is not important.The new item can go anywhere. With that in mind,
it makes sense to place the new item in the easiest location possible.

  Recall that the linked list structure provides us with only one entry point,
the head of the list. All of the other nodes can only be reached by accessing
the first node and then following next links. This means that the easiest place
to add the new node is right at the head, or beginning, of the list. In other
words, we will make the new item the first item of the list and the existing
items will need to be linked to this new first item so that they follow.

  The next methods that we will implement--length, search, and remove-- are all
based on a technique known as linked list traversal. Traversal refers to the
process of systematically visiting each node. To do this we use an external
reference that starts at the first node in the list. As we visit each node,
we move the reference the the next node by "traversing" the next reference.

  To implement the length method, we need to traverse the linked list and
keep a count of the number of nodes that occurred.

  Searching for a value in a linked list implementation of an unordered list
also uses the traversal technique. As we visit each node in the linked list we
will ask whether the data stored there matches the item we are looking for.

  The remove method requires two logical steps. First we need to traverse the
list looking for the item we want to remove. Once we find the item (recall that
we assume it is present), we must remove it. The first step is very similar to
search. Starting with an external reference set to the head of the list, we 
traverse the links until we discover the item we are looking for. Since we
assume that item is present, we know that the iteration will stop before
current gets to None. This means that we can simply use the boolean found in
the condition.

  When found becomes True, current will be a reference to the node containing
the item to be removed. But how do we remove it? In order to the node containing
we need to modify the link in the previous node so that it referes to the node
that comes after current. Unfortunately, there is no way to go backward in the
linked list. Since current refers the the node ahead of the node where we would
like to make the change, it is too late to make the necessary modifcation.

  The solution to this dilemma is to use two external references as we traverse
down the linked list. current will behave just as it did before, marking the
current location of the traverse. The new reference , which we will call
previous, will always travel one node behind current. That way, when current
stops at the node to be removed, previous will be referring to the proper place
in the linked list for the modifcation.

  Once the searching step of the remove has been completed, we need to remove
the node from the linked list. There is a special case that needs to be
addressed. If the item to be removed happens to be the first item in the list,
then current will reference the first node in the linked list. This also means
that previous will be None. In this case, it is not previous but rather the
head of the list that needs to be changed.

  The remaining methods append, insert, and pop are left as exercises.
Remember that each of these must take into account whether the change is
taking place at the head of the list or someplace else. Also, insert, index,
and pop require that we name the posistions of the list. We will assume that
position names are integers starting with 0.
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
        found = False
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

if __name__ == "__main__":
    unordered_list = UnorderedList()
    print("unordered_list.isEmpty():", unordered_list.isEmpty())
    unordered_list.add(10)
    print("unordered_list.add(10)")
    print("unordered_list.length():", unordered_list.length())
    print("unordered_list.search(10):", unordered_list.search(10))
    print("unordered_list.search(1):", unordered_list.search(1))
    print("unordered_list.remove(10):", unordered_list.remove(10))
    print("unordered_list.length():", unordered_list.length())
