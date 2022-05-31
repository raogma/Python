todo_list = [0] * 10
result = []

while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split('-', maxsplit=1)
    importance = int(tokens[0]) - 1     # importance - 1 = todo_list[index]
    note = tokens[1]
    todo_list.insert(importance, note)

for element in todo_list:
    if element != 0:
        result.append(element)

print(result)


# not fixed yet... 80 /100