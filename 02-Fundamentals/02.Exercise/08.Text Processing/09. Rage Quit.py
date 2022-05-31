msg = input().upper()
clearing_num = len(msg)
start = int()
i = -1

while i < clearing_num - 1:
    i += 1
    if msg[i].isnumeric() and msg[i + 1].isnumeric():
        msg += msg[start: i] * int(msg[i] + msg[i + 1])
        start = i + 2
        i += 1
    elif msg[i].isnumeric():
        msg += msg[start: i] * int(msg[i])
        start = i + 1
    if i == len(msg) - 2:
        break

if msg[-1].isnumeric():
    i += 1
    msg += msg[start: i] * int(msg[-1])
elif msg[-1].isalpha():
    msg += msg[-1]

print(f"""
Unique symbols used: {len(set(msg[clearing_num: len(msg)]))}
{msg[clearing_num: len(msg)]}
""")