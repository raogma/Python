rows, cols = list(map(int, input().split()))
snake = input()
mx = list()
i = 0

for row in range(rows):
    storage = list()
    append_count = 0
    while not append_count == cols:
        storage.append(snake[i])
        append_count += 1
        i += 1
        if i == len(snake):
            i = 0
    if row % 2 == 0:
        mx.append(storage)
    else:
        mx.append(storage[::-1])

[print(''.join(element)) for element in mx]