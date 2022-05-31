names = input().split(', ')
chairs = int(input())

desk = []

for i in range(len(names) - 1):
    desk.append(names[i])
    while i != len(names) - 1:
        i += 1
        desk.append(names[i])
        if len(desk) == chairs:
            print(', '.join(desk))
            desk.pop()
    desk.clear()