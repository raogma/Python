todo_list = []

while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split('-', maxsplit=1)
    importance = int(tokens[0])
    note = tokens[1]
    todo_list.append([importance, note])


def importance_fn(element):
    return element[0]


sorted_tasks = sorted(todo_list, key=importance_fn)
print([tasks[1] for tasks in sorted_tasks])
