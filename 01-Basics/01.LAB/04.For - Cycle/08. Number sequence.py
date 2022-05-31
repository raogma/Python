import sys

num_of_numbers = int(input())

min = sys.maxsize
max = -sys.maxsize

for num_of_numbers in range(1, num_of_numbers + 1):
    number = int(input())
    if number <= min:
        min = number
    if number >= max:
        max = number

print(f"Max number: {max}")
print(f"Min number: {min}")
