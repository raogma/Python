guests_count = int(input())
regular, VIP = list(), list()

for _ in range(guests_count):
    ticket = input()
    if ticket[0].isdigit():
        if ticket not in VIP:
            VIP.append(ticket)
    else:
        if ticket not in regular:
            regular.append(ticket)

while True:
    command = input()
    if command == 'END':
        break
    else:
        ticket = command

    if ticket in regular:
        regular.remove(ticket)
    elif ticket in VIP:
        VIP.remove(ticket)

print(len(VIP) + len(regular))
[print(ticket) for ticket in sorted(VIP)]
[print(ticket) for ticket in sorted(regular)]