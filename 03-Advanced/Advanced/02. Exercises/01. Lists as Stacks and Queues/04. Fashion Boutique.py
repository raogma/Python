from copy import deepcopy
from collections import deque
box = deque(input().split())
rack_capacity = int(input())
save_rack_cap = deepcopy(rack_capacity)
rack_counter = 1

while box:
    clothing = int(box.pop())
    if rack_capacity - clothing > 0:
        rack_capacity -= clothing
        continue
    elif rack_capacity - clothing == 0:
        rack_capacity -= clothing
        if box:                 # input: box = 5 6 rack: 11 za da moje ako v kutiqta nqma poveche drehi da ne vzima drug rack
            rack_counter += 1
    else:
        rack_counter += 1
        box.append(clothing)
    rack_capacity = save_rack_cap

print(rack_counter)