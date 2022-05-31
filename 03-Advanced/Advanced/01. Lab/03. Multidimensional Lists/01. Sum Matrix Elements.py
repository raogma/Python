rows, columns = list(map(int, input().split(', ')))

matrix = list()
sum = 0

for row in range(rows):
    matrix.append(list())
    line = list(map(int, input().split(', ')))
    for num in line:
        sum += num
        matrix[row].append(num)

print(sum)
print(matrix)