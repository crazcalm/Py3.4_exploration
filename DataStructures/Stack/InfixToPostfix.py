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
