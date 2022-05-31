def find_player(mx):
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            if mx[i][j] == 'P':
                return i, j


movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
coins = 0
path = []
isWon = False


mx = [input().split() for _ in range(int(input()))]
i, j = find_player(mx)

while True:
    if coins >= 100:
        isWon = True
        break
    command = input()
    if command not in movement:
        continue
    x, y = tuple(map(int, (movement[command][0], movement[command][1])))
    if x + i < 0 or x + i >= len(mx) or y + j < 0 or y + j >= len(mx[0]):
        break
    next_position = mx[x + i][y + j]
    if next_position == 'X':
        break
    else:
        coins += int(next_position)
    i, j = x + i, y + j
    path.append((i, j))

if isWon:
    print(f"You won! You've collected {coins} coins.")
else:
    coins //= 2
    print(f"Game over! You've collected {coins} coins.")


print("Your path:")
[print(f'[{el[0]}, {el[1]}]') for el in path]
