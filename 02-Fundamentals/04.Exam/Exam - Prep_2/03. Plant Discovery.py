def convert(iterable: dict):
    for key in iterable:
        x = iterable[key]['rating']
        if x:
            iterable[key]['rating'] = sum(x) / len(x)
        else:
            iterable[key]['rating'] = 0


def fill(iterable: dict, count):
    for _ in range(count):
        flower, rarity = input().split('<->')
        rarity = int(rarity)
        if flower not in iterable:
            iterable[flower] = {'rarity': rarity, 'rating': []}
            continue
        iterable[flower]['rarity'] = rarity


def printing(iterable: dict):
    res = f'Plants for the exhibition:\n'
    for key in iterable:
        res += f'- {key}; Rarity: {iterable[key]["rarity"]}; Rating: {iterable[key]["rating"]:.2f}\n'
    return res


n = int(input())
data = {}
fill(data, n)


while True:
    command = input()
    if command == 'Exhibition':
        break

    action, stuff = command.split(': ')
    if '-' in stuff:
        plant, value = stuff.split(' - ')
        value = int(value)
    else:
        plant = stuff

    if plant in data:
        if action == 'Rate':
            data[plant]['rating'].append(value)
        elif action == 'Update':
            data[plant]['rarity'] = value
        elif action == 'Reset':
            data[plant]['rating'].clear()
    else:
        print('error')

convert(data)
data = dict(sorted(data.items(), key=lambda x: (x[1]['rarity'], x[1]['rating']), reverse=True))
print(printing(data)[:-1])
