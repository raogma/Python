targets = list(map(int, input().split()))

on_point_shots = 0

while True:
    command = input()
    if command == 'End':
        print(f"Shot targets: {on_point_shots} -> {' '.join(list(map(str, targets)))}")
        break
    idx = int(command)
    if idx > len(targets) - 1:
        continue
    elif targets[idx] == -1:
        continue
    value = targets[idx]
    targets[idx] = -1
    on_point_shots += 1
    for i in range(len(targets)):
        if i == idx:
            continue
        if targets[i] != -1:
            if targets[i] > value:
                targets[i] -= value
            else:
                targets[i] += value