"""
Palindrome checker
"""
from deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for char in aString:
        chardeque.addRear(char)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        front = chardeque.removeFront()
        last  = chardeque.removeRear()

        if front != last:
            stillEqual = False

    return stillEqual

if __name__ == "__main__":
    tests = ["1", "11", "111", "1111", "10", "1111011"]

    for test in tests:
        print(palchecker(test))

