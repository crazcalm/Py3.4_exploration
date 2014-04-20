from stack import Stack

def parChecker(symbolString, open_brackets, close_brackets):
    """Check for a 1:1 ration of '([{' to "}])"

        This function takes to variables:

        symbolString --> string,
        open_brackets --> sring of open brackets
        close_brackets --> string of closing brackets"""

    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]

        if symbol in open_brackets:
            s.push(symbol)

        elif not symbol in close_brackets:
            pass

        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    """
A helper method for parChecker that makes sure the open and closing
symbols match
    """

    dic = {"(":")", "{":"}", "[":"]"}
    return dic[open] == close

if __name__ == "__main__":
    tests = [("", True), ("(", False), (")", False), ("()",True),
                 ("(())",True), ("(11(1)111)", True)]
    for test in tests:
        assert parChecker(test[0],"(",")") == test[1], "Check test cases!"
