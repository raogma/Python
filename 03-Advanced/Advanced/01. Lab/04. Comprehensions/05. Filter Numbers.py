start, end = int(input()), int(input())

filtered = list()

for x in range(start, end + 1):
    for y in range(2, 11):
        if x % y == 0:
            filtered.append(x)
            break

print(filtered)