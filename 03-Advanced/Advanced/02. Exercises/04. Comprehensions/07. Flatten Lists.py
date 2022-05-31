line = input().split('|')[::-1]
for element in line:
    [print(num, end=' ') for num in element.split()]
