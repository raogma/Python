def factorial_division(first_num, second_num):
    for i1 in range(2, first_num):
        first_num *= i1
    for i2 in range(2, second_num):
        second_num *= i2
    return f"{first_num / second_num:.2f}"


first_input = int(input())
second_input = int(input())

print(factorial_division(first_input, second_input))
