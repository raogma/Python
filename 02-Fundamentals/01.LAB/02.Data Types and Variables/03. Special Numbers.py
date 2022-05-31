numbers = int(input())


sum = 0

for number in range(1, numbers + 1):
    number_as_string = str(number)
    for digit in range(len(number_as_string)):
        sum += int(number_as_string[digit])
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{number} -> True")
        sum = 0
    else:
        print(f"{number} -> False")
        sum = 0