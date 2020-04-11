import sys

def ariphmetic(first, second, operation):
    if operation == '+' : 
        return first + second
    if operation == '-' : 
        return first - second
    if operation == '*' : 
        return first * second
    if operation == '/' : 
        return first / second
    return 'Unknown operation'

print(ariphmetic(10, 5, '+'))
print(ariphmetic(10, 5, '-'))
print(ariphmetic(10, 5, '*'))
print(ariphmetic(10, 5, '/'))
print(ariphmetic(10, 5, '?'))