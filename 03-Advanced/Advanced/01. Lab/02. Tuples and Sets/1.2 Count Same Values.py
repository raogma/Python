line = list(map(float, input().split()))

occurrences = dict()

for element in line:
    if element not in occurrences:
        occurrences[element] = 1
    else:
        occurrences[element] += 1

[print(f'{key} - {value} times') for key, value in occurrences.items()]
