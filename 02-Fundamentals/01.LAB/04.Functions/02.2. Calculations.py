def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return int(a / b)


def execution():
    mapping = [
        [add, 'add'],
        [multiply, 'multiply'],
        [divide, 'divide'],
        [subtract, 'subtract'],
    ]
    for fn, operation in mapping:
        if operation == operation_input:
            return fn(a, b)


operation_input = input()
a = int(input())
b = int(input())

print(execution())