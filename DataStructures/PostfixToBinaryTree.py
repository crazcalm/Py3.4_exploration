"""
    My goal is to right an algorithm to take a mathematical expression that
is written in postfix form and put in the binary tree (correctly).

Plan:
-----

    Use a stack to hold all of the trees needed, and then compile them into
their final single tree form.

Derived Rules (so far):
-----------------------

Ex:
---

AB+CD+*
AB+C*
ABC*+
95+86-51-*-
34+31*/83+/7+


Given that there are three or more tokens:

    1. The first operator seen will be the root of the tree.

    - If there exist two operands before this operator, then those operands
      will be the left and right children of the tree.

    - If no operands before the operator, then the operand will be the root of
      the tree and the two trees in the stack, become the left and right child
      of this tree.

    - if there only exist one operand for the operator, then the operator will
      be the root of the tree and the operand will be the left (of right [I need to check])
      of the tree and a tree from the stack will be placed as the other child.
"""

from Stack.stack import Stack
from Trees.NodesAndReferences import BinaryTree
from BuildParseTree import printexp, inorder, evaluate
import string


def recursiveHelper(tokens, stack):

    operators = "+-*/"

    print("recusive loop?")
    print("Tokens: ", tokens, "\n")

    for index, token in enumerate(tokens):

        print("current token: ", token)


        if len(tokens) >= 3:

            # case 2
            if token in operators and tokens[index -1] in string.digits \
                                and tokens[index - 2] in string.digits:
                print("1 operator and 2 operands\n\n")


                print("Tokens:", tokens)
                print("Items: ", tokens[index], tokens[index-1], tokens[index-2])

                # Making the tree
                tree = BinaryTree(token)
                tree.leftChild = BinaryTree(tokens[index - 1])
                tree.rightChild = BinaryTree(tokens[index - 2])

                # debugging
                print(printexp(tree))

                # Put tree in stack
                stack.push(tree)

                # removes items from the list
                tokens.pop(index)
                tokens.pop(index - 1)
                tokens.pop(index - 2)
                print("Aftering pop: ", tokens)

                return recursiveHelper(tokens, stack)

            elif token in operators:
                #case 3?
                print("Should be the operand and operator case")


                # maiking the tree
                tree = BinaryTree(token)
                tree.leftChild = BinaryTree(tokens[index -1])
                subtree = stack.pop()
                tree.rightChild = subtree

                # debugging
                print(printexp(tree))

                # put tree in stack
                stack.push(tree)


                # remove items from the list
                print("Tokens: ", tokens)
                print("Items: ", tokens[index], tokens[index-1])
                tokens.pop(index)
                tokens.pop(index -1)

                return recursiveHelper(tokens, stack)

        if len(tokens) == 2:

            #case 4
            if token in operators and tokens[index - 1] in string.digits:

                # maiking the tree
                tree = BinaryTree(token)
                tree.leftChild = BinaryTree(tokens[index -1])
                subtree = stack.pop()
                tree.rightChild = subtree

                # debugging
                print(printexp(tree))

                # put tree in stack
                stack.push(tree)


                #remove items from the list
                print("Tokens:", tokens)
                print("Items: ", tokens[index], tokens[index-1])
                tokens.pop(index)
                tokens.pop(index -1)

                return recursiveHelper(tokens, stack)

        if token in operators:
            # case 1
            #making tree
            tree = BinaryTree(token)
            subtree1 = stack.pop()
            subtree2 = stack.pop()
            tree.leftChild = subtree1
            tree.rightChild = subtree2

            # debugging
            print(printexp(tree))

            # put tree in stack
            stack.push(tree)

            #remove from list
            print("Tokens:", tokens)
            print("Items: ", tokens[index])
            tokens.pop(index)

            return recursiveHelper(tokens, stack)

    print("done?")
    print(stack.size())
    while stack.isEmpty() == False:
        inorder(stack.pop())
        print("\n\n")


def convertToBinaryTree(postfix):
    """
    The goal is to go from postfix to binary tree
    """

    # Puts all the tokens in a list
    tokens = postfix.split(" ")
    print("tokens: ", tokens, "\n")

    operators = "+-*/"
    

    # will fold trees
    stack = Stack()

    recursiveHelper(tokens, stack)
    return "done?????"

if __name__ == "__main__":

    equations = ["9 5 + 8 6 - 5 1 - * -", "3 4 + 3 1 * / 8 3 + / 7 +"]
    for equation in equations:
        print(convertToBinaryTree(equation))

