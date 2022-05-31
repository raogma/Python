def fill(iterable: dict, name, color, value):
    if name not in iterable:
        iterable[name] = {}
    if color not in iterable[name]:
        iterable[name][color] = value
    else:
        if iterable[name][color] < value:
            iterable[name][color] = value





dwarfs = {}

while True:
    line = input()
    if line == 'Once upon a time':
        break

    name, color, value = line.split('<:>')
    value = int(value)
