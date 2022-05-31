size = int(input())
mx = [list(map(int, input().split())) for _ in range(size)]

while True:
    command = input()
    if command == 'END':
        break
    else:
        operation, nums = command.split(' ', maxsplit=1)
        i, j, value = map(int, nums.split())
        if 0 <= i < size and 0 <= j < size:
            if operation == 'Add':
                mx[i][j] += value
            elif operation == 'Subtract':
                mx[i][j] -= value
        else:
            print('Invalid coordinates')

[print(' '.join(list(map(str, element)))) for element in mx]
