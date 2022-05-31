regular = list()
VIP = list()

while True:
    command = input()
    if command == 'PARTY':
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
        break
    else:
        ticket = command
        if ticket[0].isdigit():
            VIP.append(ticket)
        else:
            regular.append(ticket)

print(len(VIP) + len(regular))
[print(ticket) for ticket in sorted(VIP)]
[print(ticket) for ticket in sorted(regular)]