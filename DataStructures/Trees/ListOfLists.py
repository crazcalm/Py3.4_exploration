"""
                    List of Lists Representation:
                    -----------------------------

Need Functions:
---------------

- BinaryTree()

- getLeftChild()

- getRightChild()

- setRootVal()

- getRootVal()

- insertLeft(val)

- insertRight(val)


Overview:
---------

    In a tree represented by a list of lists, we will begin with Python's
list data structure and write the functions defined above.

    Although writing the interface as a set of operations on a list is a bit
different from the other abstract data types we have implemented, it is
interesting to do so because it provides us with a simple recursive data
structure that we can look at and examine directly.


Basics:
-------

    In a list of lists tree, we will store the value of the root node as the
first element of the list. The second element of the list will itself be a
list that represents the left subtree. The third element of the list will
be another list that represents the right subtree.
"""

def BinaryTree(r):
    """
    Root of the Binary Tree.
    """
    return [r, [], []]

def insertLeft(root, newBranch):
    """
        Inserts a new subtree at root[1] and, if an the root has an existing
    subtree in that location, that subtree is now the subtree of the new
    branch that you are inserting.
    """
    t = root.pop(1)
    if len(t)>1:
        root.insert(1,[newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    """
        Inserts a new subtree at root[2] and, if an the root has an existing
    subtree in that location, that subtree is now the subtree of the new
    branch that you are inserting.
    """
    t = root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal
    return root

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


if __name__ == "__main__":
    """
    I just want to know that this works.
    """

    print("List of Lists Representation Of a Binary List:")

    r = BinaryTree(3)
    print("Tree Root\n",r)

    print("\nInserting left subtree\n", insertLeft(r,4))

    print("\nInserting left subtree\n", insertLeft(r, 5))

    print("\nInserting right subtree\n", insertRight(r,6))

    print("\nInserting right subtree\n", insertRight(r,7))

    print("\nGetting the left Child of Root (as l):")
    l = getLeftChild(r)
    print("\nRoot's Left Child\n",l)

    print("\nSetting the root value for Child l,",setRootVal(l,9))

    print("\nPrinting out the whole tree\n", r)

    print("\nInserting a left subtree in l",insertLeft(l, 11))

    print("\nPrintingout the whole tree\n", r)

    print("\nGetting the right child of Root", getRightChild(r))


