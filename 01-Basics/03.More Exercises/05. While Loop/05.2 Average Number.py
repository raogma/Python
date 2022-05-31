numbers = int(input())
sum = 0

for numbers in range(1, numbers + 1):
    number = int(input())
    sum += number

average = sum / numbers
print(f"{average:.2f}")