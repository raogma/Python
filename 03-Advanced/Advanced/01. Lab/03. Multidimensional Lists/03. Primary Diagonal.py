rows = int(input())
sq_matrix = [list(map(int, input().split())) for _ in range(rows)]

total = 0

for i in range(rows):
    total += sq_matrix[i][i]

print(total)


