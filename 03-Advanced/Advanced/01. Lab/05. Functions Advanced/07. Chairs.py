def combinations(iterable, size, desk=[]):
    if len(desk) == size:
        return ', '.join(desk)

    for i in range(len(iterable)):
        desk.append(iterable[i])
        combinations(iterable[i + 1:], size, desk)
        desk.pop()


names = input().split(', ')
chairs = int(input())

print(combinations(names, chairs))