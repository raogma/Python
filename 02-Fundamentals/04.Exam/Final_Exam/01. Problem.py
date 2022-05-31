msg = input()

while True:
    command = input()
    if command == 'End':
        break
    try:
        action, value = command.split(' ', maxsplit=1)
        value = value.strip()
    except ValueError:
        msg = msg.lower()   # lowercase case
        print(msg)
        continue

    if action == 'Translate':
        old_char, new_char = value.split()
        if old_char in msg:
            msg = msg.replace(old_char, new_char)
            print(msg)
    elif action == 'Includes':
        check_str = value
        print(True if check_str in msg else False)
    elif action == 'Start':
        check_str = value
        if msg[0: len(check_str)] == check_str:
            print(True)
        else:
            print(False)
    elif action == 'FindIndex':
        char = value
        for i in range(len(msg)):
            if msg[i] == char:
                save_i = i
        print(save_i)
    elif action == 'Remove':
        start, count = map(int, value.split())
        msg = msg[:start] + msg[start + count:]
        print(msg)