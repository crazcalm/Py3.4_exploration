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
