"""
                    Demo:
                    -----

Needs to demo:
--------------

1. Math problem generator

2. Problem solver
"""

from Stack.stack import Stack
from Trees.NodesAndReferences import BinaryTree
from BuildParseTree import printexp, inorder, evaluate
from InfixToPostfix import infixToPostfix
from PostfixToBinaryTree import convertToBinaryTree
import EquationGenerator
import string

def demo():
    """
    This function will demo the eqaution generator and solver.
    """
    equation = EquationGenerator.main()

    print("\n\nEquation: ", equation, "\n\n")

    postfix_version = infixToPostfix(equation)

    print("Postfix version of equation: ", postfix_version, "\n\n")

    equation_tree = convertToBinaryTree(postfix_version)

    print("Solved equation: ", evaluate(equation_tree), '\n\n')

if __name__ == "__main__":
    demo()
