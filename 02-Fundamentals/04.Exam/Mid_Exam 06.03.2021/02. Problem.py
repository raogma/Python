shopping = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        break

    action, item = command.split(maxsplit=1)
    if action == 'Urgent':
        if item not in shopping:
            shopping.insert(0, item)
    elif action == 'Unnecessary':
        if item in shopping:
            shopping.remove(item)
    elif action == 'Correct':
        old_item, new_item = item.split()
        if old_item in shopping:
            i = shopping.index(old_item)
            shopping[i] = new_item
    elif action == 'Rearrange':
        if item in shopping:
            i = shopping.index(item)
            shopping.append(shopping.pop(i))

print(', '.join(shopping))
