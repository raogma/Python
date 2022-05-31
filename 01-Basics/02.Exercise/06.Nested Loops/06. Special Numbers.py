number = int(input())

for numbers in range(1111, 10000):
    numbers_as_string = str(numbers)
    isMagic = True
    for digit in numbers_as_string:
        if int(digit) == 0 or number % int(digit) != 0:
            isMagic = False
            break
    if isMagic:
        print(f"{numbers}", end=" ")