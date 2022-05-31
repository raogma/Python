from sys import maxsize

divisor = int(input())
bound = int(input())    #limit

max_number = -maxsize

for number in range(1, bound + 1):
    if number % divisor == 0:
        if number > max_number:
            max_number = number
print(max_number)
