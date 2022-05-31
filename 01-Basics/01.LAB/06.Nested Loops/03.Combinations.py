result = int(input())
counter = 0
sum = 0
for x1 in range(0, result + 1):
    for x2 in range(0, result + 1):
        for x3 in range(0, result + 1):
            sum = x1 + x2 + x3
            if sum == result:
                counter += 1
print(counter)

