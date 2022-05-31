from collections import deque

stations = int(input())

town = deque([[int(x) for x in input().split()] for _ in range(stations)])

for i in range(stations):
    isValid = True
    fuel = 0

    for _ in range(stations):
        station = town.popleft()
        current_fuel, distance = station
        fuel += current_fuel - distance
        if fuel < 0:
            isValid = False
        town.append(station)

    if isValid:
        print(i)
        break

    town.append(town.popleft())
