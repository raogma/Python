text = input().split()
targets = [int(num) for num in text]


while True:
    command = input()
    if command == 'End':
        break

    isInvalid = False
    command_l = command.split()
    index = int(command_l[1])
    if index > len(targets) - 1 or index < 0:
        isInvalid = True

    if command_l[0] == 'Shoot':
        if isInvalid:
            continue
        power = int(command_l[2])
        targets[index] -= power
        if targets[index] <= 0:
            targets.remove(targets[index])

    elif command_l[0] == 'Add':
        if isInvalid:
            print('Invalid placement!')
            continue
        value = int(command_l[2])
        targets.insert(index, value)

    elif command_l[0] == 'Strike':
        radius = int(command_l[2])
        end = index + radius
        start = index - radius
        if index + radius > len(targets) - 1 or start < 0 or isInvalid or radius < 0:
            print('Strike missed!')
            continue
        for i in range(start, index):
            targets.remove(targets[start])
        for i in range(index, end + 1):
            targets.remove(targets[start])

targets_str = []
for element in targets:
    targets_str.append(str(element))

print('|'.join(targets_str))
