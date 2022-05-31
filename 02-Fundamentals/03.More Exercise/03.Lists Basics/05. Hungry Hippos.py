def append_to_dict(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)


n_rows = int(input())
board = [input().split() for _ in range(n_rows)]
coordinates = {}
hippos = 0
i, j = 0, 0  #row, column

while i < len(board):
    while j < len(board[i]):
        if board[i][j] == '1':
            append_to_dict(coordinates, int(i), int(j))
            j += 1
        else:
            j += 1
    i += 1
    j = 0

block = 0

for row in coordinates:
    for index in range(len(coordinates[row])):
        if coordinates[row][index] + 1 == coordinates[row][index + 1]:
            continue
        else:
            if coordinates[row][index] in coordinates[row + 1]:
                break
            else:
                block += 1
                del coordinates[row][index]
                break
a = 8