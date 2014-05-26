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
"""

class BinarySearchTree:

    def __init_(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__inter__()
