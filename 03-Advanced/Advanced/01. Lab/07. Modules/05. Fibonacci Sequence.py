from methods.method_fib_seq import fib_seq, find_num

while True:
    command = input()
    if command == 'Stop':
        break

    action, number = command.rsplit(maxsplit=1)
    if action == 'Create Sequence':
        array = fib_seq(int(number))
        print(' '.join(list(map(str, array))))
    elif action == 'Locate':
        print(find_num(array, int(number)))
