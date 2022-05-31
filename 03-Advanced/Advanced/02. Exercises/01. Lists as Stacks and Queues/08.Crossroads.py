from collections import deque
from copy import deepcopy

green_light = int(input())
free_passage = int(input())
restore_green_light, restore_free_passage = deepcopy(green_light), deepcopy(free_passage)

traffic = deque()
passed_cars = 0
has_accident = False

while True:
    if has_accident:
        break
    command = input()
    if command == 'END':
        break
    elif command == 'green':
        green_light, free_passage = restore_green_light, restore_free_passage
        while traffic:
            car = traffic.popleft()
            if green_light - len(car) >= 0:
                green_light -= len(car)
                passed_cars += 1
                if green_light == 0:
                    break
            else:
                difference = len(car) - green_light
                if free_passage - difference >= 0:
                    free_passage -= difference
                    passed_cars += 1
                else:
                    sum = green_light + free_passage
                    has_accident = True
                break

    else:
        traffic.append(command)

if has_accident:
    print(f'''A crash happened!
{car} was hit at {car[sum]}.
''')

else:
    print(f'''Everyone is safe.
{passed_cars} total cars passed the crossroads.
''')