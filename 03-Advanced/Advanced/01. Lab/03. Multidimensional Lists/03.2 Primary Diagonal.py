rows = int(input())
sq_matrix = [list(map(int, input().split())) for _ in range(rows)]

total = 0
total += sum([sq_matrix[i][i] for i in range(rows)])

print(total)
