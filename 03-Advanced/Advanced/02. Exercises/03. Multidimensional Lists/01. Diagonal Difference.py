size = int(input())
rows, columns = size, size
sq_mx = [list(map(int, input().split())) for _ in range(rows)]
pr_diag, sec_diag = 0, 0
i, j = -1, columns

while not i == rows - 1:
    i += 1
    j -= 1
    pr_diag += sq_mx[i][i]
    sec_diag += sq_mx[i][j]

print(abs(pr_diag - sec_diag))
