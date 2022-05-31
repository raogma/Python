DATA = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, - 1)}


def find_bunnies(field):
    global DATA
    targets = []
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 'B':
                targets.append((i, j))
    return targets


def mutate_bunnies(mx):
    global DATA
    targets = find_bunnies(mx)
    for target in targets:
        i, j = target
        for key in DATA:
            x, y = DATA[key]
            if 0 <= i + x < len(mx) and 0 <= j + y < len(mx[0]):
                mx[i + x][j + y] = 'B'


def find_player(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 'P':
                return i, j


def solution(mx):
    global rows
    i, j = find_player(mx)
    for command in commands:
        x, y = DATA[command]
        if i + x < 0 or i + x >= len(mx) or j + y < 0 or j + y >= len(mx[0]):
            mx[i][j] = '.'
            mutate_bunnies(mx)
            [print(''.join(mx[row])) for row in range(rows)]
            print(f"won: {i} {j}")
            return
        if mx[i + x][j + y] == 'B': # ako igra4 nastapi zaek
            mx[i][j] = '.'
            mutate_bunnies(mx)
            [print(''.join(mx[row])) for row in range(rows)]
            print(f'dead: {i + x} {j + y}')
            return
        mx[i][j], mx[i + x][j + y] = '.', 'P'
        i, j = i + x, j + y
        mutate_bunnies(mx)
        if find_player(mx) is None: # ako zaek udari igra4
            [print(''.join(mx[row])) for row in range(rows)]
            print(f'dead: {i} {j}')
            return


rows, columns = list(map(int, input().split(' ')))
lair = [list(input()) for _ in range(rows)]
commands = list(input())

solution(lair)