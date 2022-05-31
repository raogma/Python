from re import finditer


def match(iterable: list, pattern: str):
    dictionary = {'type': str(), 'coordinates': str()}
    for element in finditer(pattern, iterable):
        element = element.group()
        if '&' in element:
            dictionary['type'] = element[1: len(element) - 1]
        else:
            dictionary['coordinates'] = element[1: len(element) - 1]

    return dictionary


def decrease(nums: list, msg: list, i, j):
    if j == len(msg):
        return
    if i == len(nums):
        i = 0
    msg[j] -= nums[i]
    decrease(nums, msg, i + 1, j + 1)


key = list(map(int, input().split(' ')))
regex = r'(&[a-zA-Z]+&)|(<[A-Z\d]+>)'

while True:
    line = input()
    if line == 'find':
        break

    line = list(map(ord, list(line)))
    decrease(key, line, 0, 0)
    line = ''.join(list(map(chr, line)))
    data = match(line, regex)
    print(f'Found {data["type"]} at {data["coordinates"]}')