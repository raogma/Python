rows, cols = list(map(int, input().split()))
mx = [input().split() for _ in range(rows)]
sq_count = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        if mx[i][j] == mx[i + 1][j] == mx[i][j + 1] == mx[i + 1][j + 1]:
            sq_count += 1
print(sq_count)
