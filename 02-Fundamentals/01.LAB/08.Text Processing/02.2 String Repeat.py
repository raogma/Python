line = input().split()

for i in range(len(line)):
    print(line[i] * len(line[i]), end='')