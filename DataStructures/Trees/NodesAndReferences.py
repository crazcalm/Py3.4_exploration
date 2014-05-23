"""
                    Nodes and References (Binary Tree):
                    -----------------------------------

Overview:
---------

    In this case we will define a class that has attributes for the root value,
as well as the left and right subtrees.Since this representation more closely
follows the object-oriented programming paradigm, we will continue to use
this representation for the remainder of the chapter.
"""
class BinaryTree:
    """
    Binary tree class (Nodes and references representation)
    """
    def __init__(self, rootObj):
        """
        Initializes the Binary Tree with a root value
        """
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """
            Inserts a new Branch to at root.leftChild. If there is an existing
        branch, then that subtree is made the leftChild of this new Branch.
        """
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        """
            Inserts a new Branch to at root.rightChild. If there is an existing
        branch, then that subtree is made the rightChild of this new Branch.
        """
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        """
        Returns the rightChild subtree
        """
        return self.rightChild

    def getLeftChild(self):
        """
        Returns the leftChild subtree
        """
        return self.leftChild

    def setRootVal(self, obj):
        """
        Sets the root of the tree
        """
        self.key = obj
        return self.getRootVal()

    def getRootVal(self):
        """
        Returns the root of the tree
        """
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

if __name__=="__main__":

    print("Binary Tree:\n")

    r = BinaryTree('a')
    print("\nSetting a as the Tree's root value:\n", r.getRootVal())

    print("\nGetting the left Child from the root\n",r.getLeftChild())

    print("\nInserting a value into the left branch\n", r.insertLeft('b'))

    print("\nGetting the value of Root's left child\n", r.getLeftChild().getRootVal())

    print("\nInserting a value into the right branch\n", r.insertRight('c'))

    print("\nGetting the value of Root's right child\n", r.getRightChild().getRootVal())

    print("\nSetting the value of Root's right Child\n", r.getRightChild().setRootVal('hello'))

    print("The external preorder is better, but I want to check that this works\n", r.preorder())

