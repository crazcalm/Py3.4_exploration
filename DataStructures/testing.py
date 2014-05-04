"""
    My gaol is to right a algorithm to convert a mathematical string to its
proper binary representation.


Plan:
-----

    Use a stack to hold all the tree needed, and them compile them into the
corrent order.

Derived Rules:
--------------

Note: The number of '(' is equal to the number of trees needed to convert the 
  equation to represent the equation as a Tree.

While reading the string:

1. if char == "(", then create a new binary Tree

2. if Char == number, then make char the child of the current tree
  (Always fill left child first).

3. if char == operator. then make operator the root of current tree.

4. if char == ")", then 
"""

from Queue.queue import Queue
from Stack.stack import Stack
from Trees.NodesAndReferences import BinaryTree
from BuildParseTree import printexp, inorder, evaluate

def convertToBinaryTree(equation):

    eStack = Stack()

    for char in equation:

        if char == "(":
            eStack.push(BinaryTree(''))
            #print("A Binary Tree was created!\n\n")

        if char in '0123456789':
            tree = eStack.pop()

            if tree:
                if tree.leftChild:
                    tree.rightChild = BinaryTree(int(char))
                    #print("A", char," was added to the leftChild\n\n")
                else:
                    #print("A", char, "was added to the rightChild\n\n")
                    tree.leftChild = BinaryTree(int(char))

            eStack.push(tree)

        if char in "+-*/":
            tree = eStack.pop()

            if tree.getRootVal() == "":
                tree.setRootVal(char)
                #print("Set the root to", char,"\n\n")

            eStack.push(tree)

        if char == ")":

            if eStack.size() == 1:
                return eStack.pop()

            else:
                subtree = eStack.pop()
                parentTree = eStack.pop()

                if parentTree.leftChild:
                    parentTree.rightChild = subtree
                else:
                    parentTree.leftChild = subtree

                eStack.push(parentTree)

def main2(equation):

    test = convertToBinaryTree(equation)
    #print(test)
    #inorder(test)
    print(printexp(test))
    print(evaluate(test))

if __name__ == "__main__":
    equation = "((5+2)*7)"

    print("\n\nTEST1:\n\n")
    test = convertToBinaryTree(equation)
    #print(test)
    #inorder(test)
    print(printexp(test))
    print(evaluate(test))

    print("---------------------------------------------")

    print("\n\nTEST2\n\n")
    equation2 = "((2+2)*(3+3))"
    test2 = convertToBinaryTree(equation2)
    #inorder(test2)
    print(printexp(test2))
    print(evaluate(test2))

