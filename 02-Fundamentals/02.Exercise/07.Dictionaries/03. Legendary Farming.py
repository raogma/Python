def append_to_dict(key, value, dictionary):
    if key not in dictionary.keys():
        dictionary[key] = value
    else:
        dictionary[key] += value


legendary = {
    'fragments': 0,
    'motes': 0,
    'shards': 0
}
legendary_items = {
    'fragments': 'Valanyr',
    'motes': 'Dragonwrath',
    'shards': 'Shadowmourne'
}
junk = {}

breakWhile = False
while True:
    line = input().lower().split()
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1]
        if material == 'shards' or material == 'fragments' or material == 'motes':
            append_to_dict(material, quantity, legendary)
            if legendary[material] >= 250:
                winner = material
                legendary[material] -= 250
                breakWhile = True
                break
        else:
            append_to_dict(material, quantity, junk)
    if breakWhile:
        break

legendary_ordered = dict(sorted(legendary.items(), key=lambda el: -el[1]))
sorted_junk = dict(sorted(junk.items(), key=lambda el: el[0]))

print(f'{legendary_items[winner]} obtained!')
[print(f'{material}: {quantity}') for material, quantity in legendary_ordered.items()]
[print(f'{material}: {quantity}') for material, quantity in sorted_junk.items()]
