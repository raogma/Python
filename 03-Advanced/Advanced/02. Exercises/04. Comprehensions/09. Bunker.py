materials = {x: [[], {'quantity': 0, 'quality': []}] for x in input().split(', ')}
lines_count = int(input())

for _ in range(lines_count):
    line = input().split(' - ')
    type, item, nums = line
    materials[type][0].append(item)
    quantity, quality = nums.split(';')
    quantity, value1 = quantity.split(':')
    quality, value2 = quality.split(':')
    materials[type][1][quantity] += int(value1)
    materials[type][1][quality].append(int(value2))

total_quantity = 0
total_quality = 0
categories = 0

for type in materials:
    categories += 1
    for key in materials[type][1]:
        if key == 'quantity':
            total_quantity += materials[type][1][key]
        elif key == 'quality':
            total_quality += sum(materials[type][1][key])

print(f'''
Count of items: {total_quantity}
Average quality: {total_quality/ categories:.2f}''')
[print(f'{element} -> {", ".join(materials[element][0])}') for element in materials]