line = input().split()

for i in range(len(line)):
    for _ in range(len(line[i])):
        print(line[i], end='')