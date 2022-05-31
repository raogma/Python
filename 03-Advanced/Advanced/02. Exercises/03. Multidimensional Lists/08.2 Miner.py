DATA = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}


def count_coals(field):
    total = 0
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 'c':
                total += 1
    return total


def find_miner(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 's':
                return i, j


def solution(mx):
    global DATA, commands, coals
    i, j = find_miner(mx)
    total_coals = count_coals(mx)
    coals = 0
    for command in commands:
        x, y = DATA[command][0], DATA[command][1]
        if 0 <= i + x < len(mx) and 0 <= j + y < len(mx[0]):
            i, j = i + x, j + y
            if mx[i][j] == 'c':
                coals += 1
                mx[i][j] = '*'
                if coals == total_coals:
                    print(f"You collected all coals! ({i}, {j})")
                    return
            elif mx[i][j] == 'e':
                print(f"Game over! ({i}, {j})")
                return
    print(f"{total_coals - coals} coals left. ({i}, {j})")


size = int(input())
commands = input().split()
field = [input().split() for _ in range(size)]

solution(field)