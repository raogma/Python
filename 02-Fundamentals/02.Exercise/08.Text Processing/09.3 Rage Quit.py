msg = input()

i = 0
start = 0
res = str()

while not i == len(msg):
    if not msg[i].isdigit():
        i += 1
    else:
        res += msg[start: i] * int(msg[i])
        i += 1
        start = i

print(f'''
Unique symbols used: {len(set(res.upper()))}
{res.upper()}
''')