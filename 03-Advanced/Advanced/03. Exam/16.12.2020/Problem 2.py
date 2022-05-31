def find_player(mx):
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            if mx[i][j] == 'P':
                return i, j


movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

res = input()
mx = [list(input()) for _ in range(int(input()))]
n = int(input())

i, j = find_player(mx)

for _ in range(n):
    command = input()
    x, y = movement[command][0], movement[command][1]
    if 0 <= i + x < len(mx) and 0 <= j + y < len(mx[0]):
        i, j = i + x, j + y
        if mx[i][j] != '-':
            res += mx[i][j]
        mx[i - x][j - y] = '-'
        mx[i][j] = 'P'
    else:
        if res:
            res = res[0: len(res) - 1]

print(res)
[print(''.join(element)) for element in mx]