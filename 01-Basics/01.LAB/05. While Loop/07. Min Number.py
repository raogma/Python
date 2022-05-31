from sys import maxsize

number = input()

min = maxsize

while number != "Stop":
    if int(number) <= min:
        min = int(number)
    number = input()
print(min)