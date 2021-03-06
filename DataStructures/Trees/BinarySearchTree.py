"""
                    Binary Search Tree:
                    -------------------

Overview:
-------

  We have already seen two different ways to get key-value pairs in a collection.
Recall that these two collections implement the 'map' abstract data type.

  The two implementations of a map ADT we discussed were binary search on a
list and hash tables.

  In this section we will study 'binary search trees' as yet another way to
map from a key to a value.

  In this case we are not interested in the exact placement of items in the
tree, but we are interested in using the binary tree to provide for efficient
searching.


Search Tree Operations:
-----------------------

  Before we look at the implementation, let's review the interface provided by
the map ADT. You will notice that the implementation is very similar to the
Python dictionary.

Map(): Creates a new, empty map.

put(key, val): Add a new key-value pair to the map. If the key is already in
               the map then replace the old value with the new value.

get(key): Given a key, return the value stored in the map or None otherwise.

del(): Delete the key-value pairs stored in the map.

len(): Return the number of key-value pairs stored in the map.

in: Return True for a statement of the form 'key in map,' if the given key
    is in the map.


Search Tree Implementation:
---------------------------

  A binary search tree relaies on the property that the keys that are less than
the parent are found in the left subtree, and the keys that are greater than the
parents are found in the right subtree.

  We call this the "bst property."

  All of the keys in the left subtree are less then the key in the root. All
of the keys in the right subtree are greater then the root.


More details:
-------------

  To implement the binary tree search, we will ise the nodes and references
approach similar to the one we used to implement the linked list, and the
expression tree.

  However, because we must be able to create and work with a binary tree that
is empty, our implementation will use two classes.

  The first class we will call 'BinarySearchTree," and the second class we will
call "TreeNode."


BinarySearchTree:
-----------------

  The BinarySearchTree class has a reference to the TreeNode that is the root
of the binary search tree.

  In most cases the external methods defined in the outer class simply check
to see if the tree is empty.

  If there are nodes in the tree, the request is just passed on to a private
method defined in the BinarySearch tree class that takes the root as a parameter.

  In the case where the tree is empty or we want to delete the key at the root
of the tree, we must take special action.


Tree Node Class:
----------------

  The TreeNode class provides many helper functions that make the work done in
the BinarySearchTree class methods much easier.

  Many of these helper functions classify a node according to its own position
as a child, (left or right) and the kind of children the node has.

  One big difference between the TreeNode and the BinarySearchTree class is
that we explicitly keep track of the parent as an attribute for the del operator.

  Another interesting aspect of the implementation of TreeNode is that we use
Python's optional paremeters. Optional parameters make it easy for us to create
a TreeNode under several different circumstances.

  Now that we have the BinarySearchTree shell and the TreeNode it is time to
write the put method that will allow us to build our binary search tree.


put and _put methods:
---------------------

  The put method is a method of the BinarySearchTree class. This method will
check to see if the tree already has a root. If there is not a root then put
will create a new TreeNode and install it as the root of the tree. If a root
node is already in place then put calls the private, recursive, helper function
_put to search the tree according to the following algorithm.

  1. Starting at the root of the tree, search the binary tree comparing the
    new key to the key of the current node. If the new key is less than the
    current node, search the left subtree. If the new key is greater than the
    current node, search the right subtree.

  2. When there is no left (or right) child to search, we have found the
    position in the tree where the new node should be installed.

  3. To add a node to the tree, create a new TreeNode object and insert the
    object at the point discovered by the previous step.


get and _get methods:
---------------------

  The get method is even easier than the put method becuse it simply searches
the tree recursively until it gets to a non-matching leaf node or finds a
matching key. When a matching key is found, the value stored in te payload of
the node is returned.


delete method:
--------------

  Finally, we turn our attention to the most challenging method in the binary
search tree, the deletion of a key.

  The first task is to find the node to delete by searching the tree. If the
tree has more than one node we search using the _get method to find the TreeNode
that needs to be removed.

  If the tree only has a single node, that means we are removing the root of
the tree, but we still must check to make sure the key of the root matches the
key of the root matches the key that is to be deleted.

  In eithe case, if the key is not found the del operator raises an error.

"""

class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasbothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __inter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                yield elem


class BinarySearchTree:

    def __init_(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1

            else:
                raise KeyError('Error, key not in tree')

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1

        else:
            raise KeyError('Error, Key not in tree')

    def remove(self, currentNode):
        if currentNode.isLeaf(): # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        elif currentNode.hasbothChildren(): # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else: # This node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                        currentNode.leftChild.payload,
                                        currentNode.leftChild.leftChild,
                                        currentNode.leftChild.rightChild)

            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                        currentNode.leftChild.payload,
                                        currentNode.leftChild.leftChild,
                                        currentNode.leftChild.rightChild)

    # study
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None

        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent

            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def put(self, key, val):
        if self.root:
            self._put(key, val, self, val)
        else:
            self.root = TreeNode(key, val)
        self.size = size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value,
                                                parent = currentNode)

        else:
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value,
                                                parent = currentNode)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None

        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None

        elif currentNode.key == key:
            return currentNode

        elif key < currentNode.key:
            return _get(key, currentNode.leftChild)

        elif key > currentNode.key:
            return _get(key, currentNode.rightChild)

        else: # All possible cases are listed above
            return None

    def __setitem__(self, k, v):
        self.put(k,v)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__inter__()
