from itertools import permutations

iterable = input().split(', ')
n = int(input())

for i in permutations(iterable, n):
    print(i)