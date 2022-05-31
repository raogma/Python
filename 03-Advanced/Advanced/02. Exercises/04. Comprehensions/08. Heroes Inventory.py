heroes = {name: [set(), 0] for name in input().split(', ')}

while True:
    command = input()
    if command == 'End':
        break
    else:
        name, item, cost = command.split('-')
        if item not in heroes[name][0]:
            heroes[name][1] += int(cost)
        heroes[name][0].add(item)

[print(f'{name} -> Items: {len(heroes[name][0])}, Cost: {heroes[name][1]}') for name in heroes]