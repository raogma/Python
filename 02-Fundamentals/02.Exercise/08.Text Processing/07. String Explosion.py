line = input() # pesho>2sis>1a>2akarate>4hexmaster

i = -1
power = int()
while i < len(line) - 1:
    i += 1
    if line[i] == '>':
        power += int(line[i + 1])
    elif power > 0:
        line = line[0: i] + line[i + 1: len(line)]
        power -= 1
        i -= 1

print(line)

