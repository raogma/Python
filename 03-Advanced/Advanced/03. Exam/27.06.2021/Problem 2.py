# 90/100 break when all targets are shot


def find_position(mx):
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            if mx[i][j] == 'A':
                return i, j


def count_targets(mx):
    total = 0
    for element in mx:
        for el in element:
            if el == 'x':
                total += 1
    return total


mx = [input().split() for _ in range(5)]
shot_targets = 0
i, j = find_position(mx)
total = count_targets(mx)
hits = []

for _ in range(int(input())):
    command = input()
    if 'move' in command:
        tokens = command.split()
        direction, value = tokens[1], tokens[2]
        value = int(value)
        if direction == 'right':
            if 0 <= j + value < len(mx):
                if mx[i][j + value] == '.':
                    mx[i][j] = '.'
                    j += value
                    mx[i][j] = 'A'

        elif direction == 'left':
            if 0 <= j - value < len(mx):
                if mx[i][j - value] == '.':
                    mx[i][j] = '.'
                    j -= value
                    mx[i][j] = 'A'

        elif direction == 'up':
            if 0 <= i - value < len(mx):
                if mx[i - value][j] == '.':
                    mx[i][j] = '.'
                    i -= value
                    mx[i][j] = 'A'

        elif direction == 'down':
            if 0 <= i + value < len(mx):
                if mx[i + value][j] == '.':
                    mx[i][j] = '.'
                    i += value
                    mx[i][j] = 'A'

    elif 'shoot' in command:
        direction = command.split()[1]
        if direction == 'right':
            for y in range(j + 1, len(mx[0])):
                if mx[i][y] == 'x':
                    shot_targets += 1
                    hits.append([i, y])
                    mx[i][y] = '.'
                    break

        elif direction == 'left':
            for y in range(j - 1, -1, -1):
                if mx[i][y] == 'x':
                    shot_targets += 1
                    hits.append([i, y])
                    mx[i][y] = '.'
                    break

        elif direction == 'up':
            for x in range(i - 1, -1, -1):
                if mx[x][j] == 'x':
                    shot_targets += 1
                    hits.append([x, j])
                    mx[x][j] = '.'
                    break
        elif direction == 'down':
            for x in range(i + 1, len(mx)):
                if mx[x][j] == 'x':
                    shot_targets += 1
                    hits.append([x, j])
                    mx[x][j] = '.'
                    break

if total == shot_targets:
    print(f"Training completed! All {total} targets hit.")
else:
    print(f"Training not completed! {total - shot_targets} targets left.")

if hits:
    [print(element) for element in hits]