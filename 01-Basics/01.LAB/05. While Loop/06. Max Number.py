from sys import maxsize

number = (input())

max = -maxsize

while number != "Stop":
    if int(number) >= max:
        max = int(number)
    number = input()
print(max)