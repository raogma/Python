from re import findall

regex = r'\d+'
line = input()

while line:
    nums = findall(regex, line)
    if len(nums) > 0:
        print(*nums, sep=' ', end=' ')
    line = input()