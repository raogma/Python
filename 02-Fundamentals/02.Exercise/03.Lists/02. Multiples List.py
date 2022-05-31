factor = int(input())
count = int(input())

number = 0
numbers = []

for _ in range(count):
    number += factor
    numbers.append(number)

print(numbers)