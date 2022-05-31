from sys import maxsize
rows, columns = list(map(int, input().split(', ')))
matrix = [list(map(int, input().split(', '))) for _ in range(rows)]

total = 0
max_sum = -maxsize

for i in range(rows):
    for j in range(columns):
        total = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if total > max_sum:
            max_sum = total
            coordinates = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
        if j == columns - 2:
            break
    if i == rows - 2:
        break

for i in range(len(coordinates)):
    print(coordinates[i], end=' ')
    if i == (len(coordinates) - 1) // 2 or i == len(coordinates) - 1:
        print()

print(max_sum)