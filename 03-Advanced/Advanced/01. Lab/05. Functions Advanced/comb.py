from itertools import combinations

iterable = input().split(', ')
n = int(input())

for i in combinations(iterable, n):
    print(i)
