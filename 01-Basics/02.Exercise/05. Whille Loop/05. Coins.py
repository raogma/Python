counter = 0
change = float(input())
change = int(change * 100)
while change > 0:
    if change - 200 >= 0:
        change -= 200
        counter += 1
        continue
    if change - 100 >= 0:
        change -= 100
        counter += 1
        continue
    if change - 50 >= 0:
        change -= 50
        counter += 1
        continue
    if change - 20 >= 0:
        change -= 20
        counter += 1
        continue
    if change - 10 >= 0:
        change -= 10
        counter += 1
        continue
    if change - 5 >= 0:
        change -= 5
        counter += 1
        continue
    if change - 2 >= 0:
        change -= 2
        counter += 1
        continue
    if change - 1 >= 0:
        change -= 1
        counter += 1
        continue
else:
    print(int(counter))