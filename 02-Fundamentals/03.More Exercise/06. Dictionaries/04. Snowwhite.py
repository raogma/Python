def sort_by_physics(iterable: tuple):
    for key in iterable[1]:
        return -iterable[1][key]


def sort_by_count(iterable: tuple):
    return -len(iterable[1])


def printing(iterable: dict):
    res = str()
    iterable = dict(sorted(iterable.items(), key=lambda x: (sort_by_physics(x), sort_by_count(x))))
    for key in iterable:
        for subkey in iterable[key]:
            res += f'({key}) {subkey} <-> {iterable[key][subkey]}\n'
    return res


def fill(iterable: dict, color, name, physics):
    if color not in iterable:
        iterable[color] = {}
    if name in iterable[color]:
        if physics > iterable[color][name]:
            iterable[color][name] = physics
    else:
        iterable[color][name] = physics


data = {}

while True:
    command = input()
    if command == 'Once upon a time':
        break

    name, color, physics = command.split(' <:> ')
    physics = int(physics)
    fill(data, color, name, physics)

print(printing(data))
