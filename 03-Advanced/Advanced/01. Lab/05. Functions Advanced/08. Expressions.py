from itertools import permutations

nums = input().split(', ')
n = len(nums)

total = set(permutations(['-'] * n + ['+'] * n, n))

for element in total:
    element = list(element)
    res = []
    for sign, num in zip(element, nums):
        res.append(sign)
        res.append(num)
    res = "".join(res)
    print(f'{res}={eval(res)}')
