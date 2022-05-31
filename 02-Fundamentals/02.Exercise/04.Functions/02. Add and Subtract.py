def sum_numbers(a, b):
    return a + b


def subtract(x, y):
    return x - y


def add_and_subtract(f, g, h):
    return subtract(sum_numbers(f, g), h)


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))
