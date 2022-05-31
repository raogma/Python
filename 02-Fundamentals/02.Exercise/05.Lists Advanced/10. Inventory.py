items = input().split(', ')

inventory = [i for i in items]
inventory_str = ''

while True:
    command = input()
    if command == 'Craft!':
        break
    command_l = command.split(' - ')
    item = command_l[1]
    if command_l[0] == 'Collect':
        if item not in inventory:
            inventory.append(item)
    elif command_l[0] == 'Drop':
        if item in inventory:
            inventory.remove(item)
    elif command_l[0] == 'Combine Items':
        item_l = item.split(':')
        old_item = item_l[0]
        new_item = item_l[1]
        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)
    elif command_l[0] == 'Renew':
        if item in inventory:
            inventory.append(item)
            inventory.remove(item)

for j in range(len(inventory)):
    if j == len(inventory) - 1:
        print(inventory[j])
    else:
        print(inventory[j], end=', ')
