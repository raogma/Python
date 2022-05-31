dwarfs = {}
colors = {}

while True:
    command = input()
    if command == 'Once upon a time':
        break
    name, color, physics = command.split(' <:> ')
    physics = int(physics)
    id = name + ":" + color
    if id not in dwarfs:
        if color not in colors:
            colors[color] = 1
        else:
            colors[color] += 1
        dwarfs[id] = [0, color]
    dwarfs[id][0] = max([dwarfs[id][0], physics])

sorted_dwarfs = dict(sorted(dwarfs.items(), key=lambda x: (x[1][0], colors[x[1][1]]), reverse=True))
for key, value in sorted_dwarfs.items():
    tokens = key.split(":")
    print(f"({tokens[1]}) {tokens[0]} <-> {value[0]}")