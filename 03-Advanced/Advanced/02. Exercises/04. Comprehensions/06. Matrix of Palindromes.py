rows, cols = map(int, input().split())

mx = [[] for _ in range(rows)]

counter = 0
for r in range(rows):
    for c in range(cols):
        combination = chr(r + 97) + chr(r + c + 97) + chr(r + 97)
        mx[counter].append(combination)
        if c == cols - 1:
            counter += 1

[print(' '.join(element)) for element in mx]