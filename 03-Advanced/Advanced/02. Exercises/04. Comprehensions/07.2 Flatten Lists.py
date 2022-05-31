line = input()
result = []
for element in line.split('|')[::-1]:
    for num in element.split(' '):
        if num != ' ':
            result.append(num)
print(' '.join(result))