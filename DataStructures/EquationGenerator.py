"""
Goal:
-----

    Create a algebraic equation generator with balanced paratheses
"""
from Queue.queue import Queue
from Stack.stack import Stack
import random

#I had trouble importing this
def parChecker(symbolString, open_brackets, close_brackets):
    """Check for a 1:1 ration of '([{' to "}])"

        This function takes to variables:

        symbolString --> string,
        open_brackets --> sring of open brackets
        close_brackets --> string of closing brackets"""

    s = Stack()
    balanced = True
    index = 0

    print(symbolString)

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
# end of parchecker


def randomNumbersQueue(limit):
    nQueue = Queue()

    for x in range(limit):
        num = random.randint(0,10)
        nQueue.enqueue(str(num))

    return nQueue

def equationGenerator(numList):

    operators = ['+', '-', '*', '/']

    if numList.size() == 1:
        return numList.dequeue() + ")"

    if numList.size() == 2:
        return "(" + numList.dequeue() + random.choice(operators) + numList.dequeue() + ")"

    if numList.size() > 2:
        return "(" + numList.dequeue() + random.choice(operators) + numList.dequeue() + ")" + random.choice(operators) + equationGenerator(numList)

def balanceParentheses(equation):
    if parChecker(equation,"(",")"):
        print(equation)
        return equation
    else:
        equation = "(" + equation
        print(equation)
        return parChecker(equation,"(",")")

if __name__ == "__main__":
    print("\nTest1\n\n")
    test = randomNumbersQueue(4)
    #print(test)
    test_str = equationGenerator(test)
    test_str = "(" + test_str + ")"
    print(test_str)
    print(balanceParentheses(test_str))

    print("\n\nTest 2\n\n")
    test2 = randomNumbersQueue(5)
    test2_str = equationGenerator(test2)
    print(balanceParentheses(test2_str))
