numbers = int(input())
sum = 0
counter = 0

while numbers > 0:
    number = int(input())
    sum += number
    numbers -= 1
    counter += 1
else:
    average = sum / counter
    print(f"{average:.2f}")