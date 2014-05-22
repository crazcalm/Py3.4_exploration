"""
                    Prefix and Postfix expressions (math):
                    --------------------------------------

Background:
-----------

    Changes to the posistion of the operator with respect to the operands create
two new expression formats, 'prefix' and 'postfix.'

Prefix: A prefix expression requires that all operators proceed the two operands
        that they work on.

Postfix: A postfix expression requires that its operators come after the
         corresponding operands.

Ex:
---

    A+B*C woould be written as +A*BC in prefix. The multiplication operator comes
immediately before the operands B and C, denoting that * has precedence over +.
The addition operator then appears before the A and the result of the multiplication.

    In postfix, the expression would be ABC*+. Again, the order of operations
is preserved since the * appears immediately after the B and C, denoting that
* has precedence, with + coming after.

"""

from stack import Stack
import string

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec['-'] = 2
    prec['('] = 1

    opStack = Stack()
    postfixList = []

    tokenList = infixexpr.split()

    for token in tokenList:
        if token in string.ascii_uppercase:
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
              (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return "".join(postfixList)

if __name__ == "__main__":
    print(infixToPostfix("( A + B ) * ( C + D )"))
    print(infixToPostfix("( A + B ) * C"))
    print(infixToPostfix("A + B * C"))
