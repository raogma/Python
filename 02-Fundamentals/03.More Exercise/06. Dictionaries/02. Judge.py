from collections import OrderedDict


def calculate_points(iterable):
    res = {}
    for key in iterable:              # len's not working properly
        for subkey in iterable[key]:
            if subkey not in res:
                res[subkey] = iterable[key][subkey]
            else:
                res[subkey] += iterable[key][subkey]
    return res


def printing(iterable):
    res = str()
    for key in iterable:
        count = 0
        res += f'{key}: {len(iterable[key])} participants\n'
        for subkey in dict(sorted(iterable[key].items(), key=lambda el: (-el[1], el[0]))):
            count += 1
            res += f'{count}. {subkey} <::> {iterable[key][subkey]}\n'

    users = calculate_points(iterable)
    res += f'Individual standings:\n'
    count = 0
    for user in dict(sorted(users.items(), key=lambda el: (-el[1], el[0]))):
        count += 1
        res += f'{count}. {user} -> {users[user]}\n'

    return res


data = OrderedDict()
while True:
    command = input()
    if command == 'no more time':
        break
    user, contest, points = command.split(' -> ')
    points = int(points)

    if contest not in data:
        data[contest] = {}

    if user in data[contest]:
        if points > data[contest][user]:
            data[contest][user] = points
    else:
        data[contest][user] = points

print(printing(data))
