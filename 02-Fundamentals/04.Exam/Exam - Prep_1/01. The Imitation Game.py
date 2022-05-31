msg = input()

while True:
    data = input()
    if data == 'Decode':
        print(f'The decrypted message is: {msg}')
        break

    command, value = data.split('|', maxsplit=1)

    if command == 'Move':
        value = int(value)
        lett = msg[:value]
        msg = msg[value:] + lett

    elif command == 'Insert':
        position, lett = value.split('|', maxsplit=1)
        position = int(position)
        msg = msg[:position] + lett + msg[position:]

    elif command == 'ChangeAll':
        old_lett, new_lett = value.split('|', maxsplit=1)
        for i in range(len(msg)):
            if msg[i] == old_lett:
                msg = msg[:i] + new_lett + msg[i + 1:]
