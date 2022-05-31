forces = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if '|' in command:
        forceSide, forceUser = command.split(' | ')
    elif '->' in command:
        forceUser, forceSide = command.split(' -> ')

    if forceSide not in forces.keys():
        forces[forceSide] = []

    isFound = False
    for side, users in forces.items():
        if forceUser in users:
            isFound = True
            save_side = side
            break

    if not isFound:
        forces[forceSide].append(forceUser)
        if '->' in command:
            print(f"{forceUser} joins the {forceSide} side!")

    elif isFound and '->' in command:
        forces[save_side].remove(forceUser)
        forces[forceSide].append(forceUser)
        print(f"{forceUser} joins the {forceSide} side!")

for forceSide in dict(sorted(forces.items(), key=lambda el: (-len(el[1]), el[0]))):
    if len(forces[forceSide]) > 0:
        print(f'Side: {forceSide}, Members: {len(forces[forceSide])}')
        [print(f'! {forceUser}') for forceUser in sorted(forces[forceSide])]