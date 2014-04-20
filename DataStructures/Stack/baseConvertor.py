from stack import Stack

def baseConverter(decNumber, base):
    """
    Converts positive number into their base number form. Works for base 
1 to 16.
    """

    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

if __name__ == "__main__":
    for num in range(2,10,1):
        answer = baseConverter(num,2)
        assert int(answer,2) == num
