rows = int(input())
mx = [list(map(int, input().split(', '))) for _ in range(rows)]

i = 0
while i != rows:
    [mx.append(symbol) for symbol in mx.pop(0)]
    i += 1

print(mx)
