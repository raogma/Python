line = list(map(float, input().split()))

while line:
    occurrences, i = 0, 0
    num = line[0]

    while not i == len(line):
        if num == line[i]:
            occurrences += 1
        i += 1
    line = [x for x in line if x != num]
    print(f'{num} - {occurrences} times')
