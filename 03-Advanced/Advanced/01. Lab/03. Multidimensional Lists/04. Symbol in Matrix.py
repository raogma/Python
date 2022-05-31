rows = int(input())
sq_matrix = [list(input()) for _ in range(rows)]
searched_symbol = input()

isFound = False

for i in range(rows):
    for j in range(rows):
        if searched_symbol in sq_matrix[i][j]:
            isFound = True
            coordinates = i, j
            break
    if isFound:
        break

if isFound:
    print(coordinates)
else:
    print(f'{searched_symbol} does not occur in the matrix')