"""
                            Parse Tree:
                            -----------

Basics:
-------

    Parse trees can be used to represent real-world constructions like sentences
or mathematical expressions.


Task:
-----

    In the rest of this section we are going to examine parse trees in detail.
In particular we will look at:

1. How to build a parse tree from a fully parathesized mathematical expression.

2. How to evaluate the expression stored in a parsed tree.

3. How to recover the original mathematical expression from a parse tree.


Steps:
------

    The first step in building a parse tree is to break up the expression
string into a list of tokens. There are four different kind of tokens to consider:
left parentheses, right parentheses, operators, and operands.

    We know that whenever we read a left parathesis we are starting a new expression,
and hence we should create a new tree to correspond to that expression.
Conversely, whenever we read a right paraenthesis, we have finished an expression.

    We also know that operands are going to be leaf nodes and children of their
operators.

    Finally, we know that every operator is going to have both a left and right
child.


Rules:
------

    Using the information from above we can define four rules as follows.

1.  If the current token is a '(', add a new node as the left child of the
  current node, and decend to the left child.

2.  If the current token is in the list ['+', '-', '/', '*'], set the root
  value of the current node to the operator represented by the current token.
  Add a new node as the right child of the current node and descend to the right.

3.  If the current token is a number, set the root value of the current node
  to the number and return to the parent.

4.  If the current token is ')', go to the parent of the current node.
"""
from Stack.stack import Stack
from Trees.NodesAndReferences import BinaryTree
import operator

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree  = BinaryTree('')
    pStack.push(eTree)

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i not in "+-*/)":
            currentTree.setRootVal(eval(i))
            parent = pStack.pop()
            currentTree = parent

        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ")":
            currentTree = pStack.pop()

        else:
            raise ValueError('Unknown Operator: ' + i)

    return eTree

def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):

    if tree != None:

        if tree.leftChild:
            inorder(tree.getLeftChild())

        print(tree.getRootVal())

        if tree.rightChild:
            inorder(tree.getRightChild())

def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}

    res1 = None
    res2 = None

    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())



        if res1 and res2:
            print(opers[tree.getRootVal()](res1, res2))
            return opers[tree.getRootVal()](res1, res2)
        else:
            #print(tree.getRootVal())
            return tree.getRootVal()

def printexp(tree):
    sVal = ""
    if tree:
        if tree.leftChild:
            sVal = "(" + printexp(tree.getLeftChild())
        else:
            sVal = printexp(tree.getLeftChild())

        sVal = sVal + str(tree.getRootVal())

        if tree.rightChild:
            sVal = sVal + printexp(tree.getRightChild()) +")"
        else:
            sVal = sVal + printexp(tree.getRightChild())
    return sVal

def main2(x):
    print(evaluate(x))
    print(printexp(x))
    print(postordereval(x))


if __name__ == "__main__":
    x = BinaryTree('*')
    x.insertLeft('+')
    l = x.getLeftChild()
    l.insertLeft(4)
    l.insertRight(5)
    x.insertRight(7)

    preorder(x)
    postorder(x)
    inorder(x)

    print(evaluate(x))

    print(printexp(x))
    print(postordereval(x))
