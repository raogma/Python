N = int(input())
M = int(input())
S = int(input())

for numbers in range(M, N - 1, - 1):
    if numbers % 2 == 0 and numbers % 3 == 0:
        if numbers == S:
            break
        print(numbers, end=" ")
