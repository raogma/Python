def check_surroundings(mx, i, j):
    for m in range(i - 1, i + 2):
        if 0 <= m < len(mx):
            if mx[m][j] == '1' and (m, j) != (i, j):
                mx[m][j] = 'x'
                check_surroundings(mx, m, j)

    for n in range(j - 1, j + 2):
        if 0 <= n < len(mx[0]):
            if mx[i][n] == '1' and (i, n) != (i, j):
                mx[i][n] = 'x'
                check_surroundings(mx, i, n)


sq_mx = [input().split() for _ in range(int(input()))]
count = 0
for y in range(len(sq_mx)):
    for x in range(len(sq_mx[0])):
        if sq_mx[y][x] == '1':
            sq_mx[y][x] = 'x'
            check_surroundings(sq_mx, y, x)
            count += 1

print(count)