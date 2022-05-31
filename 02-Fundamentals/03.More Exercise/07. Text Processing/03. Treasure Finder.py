def decrease(nums: list, msg: list, i, j):
    if j == len(msg):
        return
    if i == len(nums):
        i = 0
    msg[j] -= nums[i]
    decrease(nums, msg, i + 1, j + 1)


def find_indices(txt, searched_symbol):
    data = []
    for i in range(len(txt)):
        if txt[i] == searched_symbol:
            data.append(i)
    return data


def match(txt):
    start, end = find_indices(txt, '&')
    type = txt[start + 1: end]
    start = find_indices(txt, '<')[0]
    end = find_indices(txt, '>')[0]
    coordinates = txt[start + 1: end]
    return f'Found {type} at {coordinates}'


key = list(map(int, input().split(' ')))

while True:
    line = input()
    if line == 'find':
        break

    line = list(map(ord, list(line)))
    decrease(key, line, 0, 0)
    line = ''.join(list(map(chr, line)))

    print(match(line))