stops = input()

while True:
    command = input()
    if command == 'Travel':
        print(f"Ready for world tour! Planned stops: {stops}")
        break

    action, value = command.split(':', maxsplit=1)

    if action == 'Add Stop':
        index, word = value.split(':')
        index = int(index)
        if 0 <= index < len(stops):
            stops = stops[:index] + word + stops[index:]
        print(stops)
    elif action == 'Remove Stop':
        start, end = map(int, value.split(':'))
        if 0 <= start < len(stops) and 0 <= end < len(stops):
            stops = stops[:start] + stops[end + 1:]
        print(stops)
    elif action == 'Switch':
        old_word, new_word = value.split(':')
        stops = stops.replace(old_word, new_word)
        print(stops)