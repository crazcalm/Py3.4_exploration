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
from InfixToPostfix import infixToPostfix
import EquationGenerator
import string


def recursiveHelper(tokens, stack):

    operators = "+-*/"

    for index, token in enumerate(tokens):

        if len(tokens) >= 3:

            # case 2
            if token in operators and tokens[index -1] in string.digits \
                                and tokens[index - 2] in string.digits:

                # Making the tree
                tree = BinaryTree(token)
                tree.rightChild = BinaryTree(int(tokens[index - 1]))
                tree.leftChild = BinaryTree(int(tokens[index - 2]))

                # debugging
                print(printexp(tree))

                # Put tree in stack
                stack.push(tree)

                # removes items from the list
                tokens.pop(index)
                tokens.pop(index - 1)
                tokens.pop(index - 2)

                return recursiveHelper(tokens, stack)

            elif token in operators and tokens[index-1] in string.digits:
                #case 3

                # maiking the tree
                tree = BinaryTree(token)
                tree.rightChild = BinaryTree(int(tokens[index -1]))
                subtree = stack.pop()
                tree.leftChild = subtree

                # debugging
                print(printexp(tree))

                # put tree in stack
                stack.push(tree)

                # remove items from the list
                tokens.pop(index)
                tokens.pop(index -1)

                return recursiveHelper(tokens, stack)

        if len(tokens) == 2:

            #case 4
            if token in operators and tokens[index - 1] in string.digits:

                # maiking the tree
                tree = BinaryTree(token)
                tree.rightChild = BinaryTree(int(tokens[index -1]))
                subtree = stack.pop()
                tree.leftChild = subtree

                # debugging
                print(printexp(tree))

                # put tree in stack
                stack.push(tree)

                #remove items from the list
                tokens.pop(index)
                tokens.pop(index -1)

                return recursiveHelper(tokens, stack)

        if token in operators:
            # case 1
            #making tree
            tree = BinaryTree(token)
            subtree1 = stack.pop()
            subtree2 = stack.pop()
            tree.rightChild = subtree1
            tree.leftChild = subtree2

            # debugging
            print("Below is the rebuilding of the expression from the binary"\
                    + "tree\n\n")
            print(printexp(tree))

            # put tree in stack
            stack.push(tree)

            #remove from list
            tokens.pop(index)

            return recursiveHelper(tokens, stack)

    #print("done?")
    #print(stack.size())
    return stack.pop()


def convertToBinaryTree(postfix):
    """
    The goal is to go from postfix to binary tree
    """

    # Puts all the tokens in a list
    tokens = list(postfix)
    print("tokens: ", tokens, "\n")

    operators = "+-*/"
    

    # will fold trees
    stack = Stack()

    return recursiveHelper(tokens, stack)


if __name__ == "__main__":

    equations = ["95+86-51-*-", "34+31*/83+/7+"]
    for equation in equations:
        print(convertToBinaryTree(equation))

    for x in range(3):
        test = EquationGenerator.main()
        print(test)
        test1 = infixToPostfix(test)
        print(test1)
        test2 = convertToBinaryTree(test1)
        print(test2)
        print(evaluate(test2))

