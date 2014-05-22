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
        num = random.randint(1,10)
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
        #print(equation)
        return equation
    else:
        equation = "(" + equation
        #print(equation)
        if parChecker(equation,"(",")"):
            return equation
        else:
            balanceParentheses(equation)

def main():
    num = int(input("\n\nEnter the number of digits that you want in the equation: "))

    print("\n\n")

    if num % 2 == 0:
        test = randomNumbersQueue(num)
        test_str = equationGenerator(test)
        test_str = "(" + test_str + ")"
        #print("Equation: ", test_str, "\n\n")
        return (balanceParentheses(test_str))

    else:
        test2 = randomNumbersQueue(num)
        test2_str = equationGenerator(test2)
        test2 = balanceParentheses(test2_str)
        #print("Equation: ", test2, "\n\n")
        return (test2)

if __name__ == "__main__":
    print(main())
    print("\n\n")
