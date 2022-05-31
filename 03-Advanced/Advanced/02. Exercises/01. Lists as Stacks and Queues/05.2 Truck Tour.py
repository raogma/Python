from collections import deque
from copy import deepcopy
n_pumps = int(input())
town = deque(list(map(lambda x: int(x), input().split())) for _ in range(n_pumps))
copy_town = deepcopy(town)

excess_fuel, counter = 0, 0
while True:
    counter += 1
    station = town.popleft()
    obtainable_fuel, distance = station
    obtainable_fuel += excess_fuel
    if obtainable_fuel >= distance:
        excess_fuel = obtainable_fuel - distance
        if counter == 1:
            save_index = copy_town.index(station)
    else:
        counter, excess_fuel = 0, 0
    town.append(station)
    if counter == n_pumps:
        print(save_index)
        break