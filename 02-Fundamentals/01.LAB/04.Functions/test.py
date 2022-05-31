input_operator = input()
first_num = int(input())
second_num = int(input())


def calculator(a, b, operator):
    result = None
    if operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    elif operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a / b
    return int(result)


print(calculator(input_operator, first_num, second_num))
