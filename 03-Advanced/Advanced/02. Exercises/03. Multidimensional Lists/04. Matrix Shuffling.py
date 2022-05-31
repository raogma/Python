rows, cols = list(map(int, input().split()))
mx = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == 'END':
        break
    else:
        if 'swap' not in command:
            print('Invalid input!')
            continue
        operation, coordinates = command.split(' ', maxsplit=1)
        coordinates = coordinates.split()
        if len(coordinates) != 4:
            print('Invalid input!')
            continue
        row1, col1, row2, col2 = tuple(map(int, coordinates))
        if (row1 >= len(mx) or row2 >= len(mx)) or (col1 >= len(mx[0]) or col2 >= len(mx[0])):
            print('Invalid input!')
            continue
        mx[row1][col1], mx[row2][col2] = mx[row2][col2], mx[row1][col1]
        [print(' '.join(element)) for element in mx]

