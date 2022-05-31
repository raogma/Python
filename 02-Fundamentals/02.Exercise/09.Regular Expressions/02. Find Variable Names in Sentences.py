from re import findall

regex = r'(?<=\b_)[A-Za-z0-9]+\b'

names = findall(regex, input())
print(*names, sep=',')
