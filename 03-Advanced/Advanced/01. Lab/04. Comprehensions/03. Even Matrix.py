rows = int(input())
mx = [list(map(int, input().split(', '))) for _ in range(rows)]

for i in range(len(mx)):
    mx[i] = [num for num in mx[i] if num % 2 == 0]

print(mx)
