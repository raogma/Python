def explode(mx, size, value, starting_row_index,  starting_col_index):
    for r in range(starting_row_index - 1, starting_row_index + 2):
        if 0 <= r < size:
            for c in range(starting_col_index - 1, starting_col_index + 2):
                if 0 <= c < size:
                    if mx[r][c] > 0:
                        mx[r][c] -= value


def count_func(mx, size):
    alive = 0
    total = 0
    for i in range(size):
        for j in range(size):
            if mx[i][j] > 0:
                alive += 1
                total += mx[i][j]
    return alive, total


size = int(input())
sq_mx = [list(map(int, input().split())) for _ in range(size)]
coordinates = input().split()

for element in coordinates:
    i, j = tuple(map(int, element.split(',')))
    value = sq_mx[i][j]
    if value > 0:
        explode(sq_mx, size, value, i, j)

result = count_func(sq_mx, size)

print(f'''Alive cells: {result[0]}
Sum: {result[1]}''')
[print(' '.join((map(str, row)))) for row in sq_mx]

## За р-нието е важно ако някоя клетка е станала <= 0 да не се намаля повече
