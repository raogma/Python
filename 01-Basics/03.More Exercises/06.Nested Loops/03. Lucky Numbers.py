N = int(input())

first_sum = 0
second_sum = 0
isDigit_in_range = True

for number in range(1000, 10000):
    number_as_string = str(number)
    for digit in range(0, 4):
        if int(number_as_string[digit]) == 0:
            isDigit_in_range = False
            break
        if digit <= 1:
            first_sum += int(number_as_string[digit])
        else:
            second_sum += int(number_as_string[digit])
    if first_sum == second_sum and N % first_sum == 0 and isDigit_in_range:
        print(number, end=" ")
    first_sum = 0
    second_sum = 0
    isDigit_in_range = True
