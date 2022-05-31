from itertools import combinations
names = input().split(', ')
chairs = int(input())

for x in combinations(names, chairs):
    print(', '.join(x))
