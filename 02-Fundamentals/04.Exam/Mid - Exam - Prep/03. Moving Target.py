targets = list(map(int, input().split()))

while True:
    command = input()
    if command == 'End':
        print(f'{"|".join(list(map(str, targets)))}')
        break
    action, *nums = command.split()
    idx, value = list(map(int, nums))
    if action == 'Shoot':
        if 0 <= idx < len(targets):
            targets[idx] -= value
            if targets[idx] <= 0:
                targets.pop(idx)
    elif action == 'Add':
        if 0 <= idx < len(targets):
            targets.insert(idx, value)
        else:
            print("Invalid placement!")
    elif action == 'Strike':
        if idx - value >= 0 and idx + value < len(targets):
            for i in range(idx - value, idx + value + 1):
                targets[i] = 0
            targets = [num for num in targets if num != 0]
        else:
            print("Strike missed!")