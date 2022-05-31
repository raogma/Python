def get_conflicts(mx, size, r, c):
    conflicts = 0
    movement = {
        r + 1: [c + 2, c - 2],
        r - 1: [c + 2, c - 2],
        r + 2: [c + 1, c - 1],
        r - 2: [c + 1, c - 1],
    }
    for key, value in movement.items():
        if 0 <= key < size:
            for element in value:
                if 0 <= element < size:
                    if mx[key][element] == 'K':
                        conflicts += 1
    return conflicts


rows = int(input())
sq_mx = [list(input()) for _ in range(rows)]

removed = 0

while True:
    max_conflicts = 0
    for i in range(rows):
        for j in range(rows):
            if sq_mx[i][j] == 'K':
                conflicts = get_conflicts(sq_mx, rows, i, j)
                if conflicts > max_conflicts:
                    max_conflicts = conflicts
                    save = i, j
    if max_conflicts == 0:
        break
    sq_mx[save[0]][save[1]] = '0'
    removed += 1

print(removed)
