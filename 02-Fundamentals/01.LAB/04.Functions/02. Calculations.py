def calculator(operator, first_num, second_num):
    result = None
    if operator == 'add':
        result = first_num + second_num
    elif operator == 'subtract':
        result = first_num - second_num
    elif operator == 'multiply':
        result = first_num * second_num
    elif operator == 'divide':
        result = first_num / second_num
    return int(result)


operator = input()
first_num = int(input())
second_num = int(input())
print(calculator(operator, first_num, second_num))
