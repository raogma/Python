factor = int(input())
count = int(input())

numbers = []

for number in range(factor, factor * count + 1, factor):
    numbers.append(number)

print(numbers)