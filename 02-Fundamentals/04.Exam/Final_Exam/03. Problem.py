def printing(iterable: dict, n):
    res = str()
    for key in iterable:
        res += f'{key}: ' + ', '.join(iterable[key]) + f'\n'
    res += f'Unliked meals: {n}'
    return res


data = {}
count = 0

while True:
    command = input()
    if command == 'Stop':
        break

    evaluation, name, meal = command.split('-')

    if evaluation == 'Like':
        if name not in data:
            data[name] = []
        if meal not in data[name]:
            data[name].append(meal)

    elif evaluation == 'Unlike':
        if name not in data:
            print(f'{name} is not at the party.')
            continue
        if meal not in data[name]:
            print(f"{name} doesn't have the {meal} in his/her collection.")
            continue
        print(f"{name} doesn't like the {meal}.")
        data[name].remove(meal)
        count += 1

data = dict(sorted(data.items(), key=lambda el: (-len(el[1]), el[0])))

print(printing(data, count))