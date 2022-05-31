def fill(iterable: dict, player, distance):
    if player in iterable:
        iterable[player] += distance
    else:
        iterable[player] = distance


def printing(iterable: dict, info: dict, i):
    res = str()
    for key in iterable:
        i += 1
        res += f'{i}{info[i]} place: {key}\n'
        if i == 3:
            return res


participants = input().split(', ')
data = {}
suffix = {
    1: 'st',
    2: 'nd',
    3: 'rd',
}

while True:
    line = input()
    if line == 'end of race':
        break

    player = ''.join([x for x in line if x.isalpha()])
    distance = sum([int(x) for x in line if x.isdigit()])
    if player in participants:
        fill(data, player, distance)

data = dict(sorted(data.items(), key=lambda x: -x[1]))
print(printing(data, suffix, 0))