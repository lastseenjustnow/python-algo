import graph as g


# Challenge 1: Find the Greatest Common Divisor
def gcd(testVariable1, testVariable2):
    # Euclidian algorithm
    if testVariable1 == testVariable2:
        return testVariable1
    min_var = min(testVariable1, testVariable2)
    diff = max(testVariable1, testVariable2) - min_var
    return gcd(min_var, diff)


# Challenge 2: Pascal's Triangle
def printPascal(testVariable):
    if testVariable < 2:
        return [1] * (testVariable + 1)
    else:
        prev = printPascal(testVariable - 1)
        result = [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]
        return result


# Challenge 3: Convert Decimal Number to Binary Number
def decimalToBinary(testVariable):
    if testVariable == 0:
        return '0'

    init = 0
    while testVariable >= 2 ** init:
        init += 1

    def rec(i: int, residual: int, result: str):
        if i == -1:
            return result
        if residual >= 2 ** i:
            return rec(i - 1, residual - 2 ** i, result + '1')
        return rec(i - 1, residual, result + '0')

    return rec(init - 1, testVariable, '')


# Challenge 2: Balance Parenthesis
def balanced(testVariable, startIndex=0, currentIndex=0):
    if startIndex == len(testVariable):
        return currentIndex == 0
    if currentIndex < 0:
        return False
    if testVariable[startIndex] == '(':
        return balanced(testVariable, startIndex + 1, currentIndex + 1)
    if testVariable[startIndex] == ')':
        return balanced(testVariable, startIndex + 1, currentIndex - 1)
    return balanced(testVariable, startIndex + 1, currentIndex)


# Challenge 2: Reverse a Stack
def reverse(testVariable):
    def insertAtBottom(stack, x):
        if len(stack) == 0:
            stack.append(x)
        else:
            h = stack.pop()
            insertAtBottom(stack, x)
            stack.append(h)

    if not len(testVariable) == 0:
        head = testVariable.pop()
        reverse(testVariable)
        insertAtBottom(testVariable, head)
