rows, columns = list(map(int, input().split(', ')))

matrix = [list(map(int, input().split())) for _ in range(rows)]
total = 0

for col in range(columns):
    for row in range(rows):
        total += matrix[row][col]
    print(total)
    total = 0