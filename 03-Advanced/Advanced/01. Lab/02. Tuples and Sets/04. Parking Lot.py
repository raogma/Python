car_lot = list()

while True:
    command = input()
    if command == 'END':
        break
    else:
        action, l_plate = command.split(', ')

    if action == 'IN':
        car_lot.append(l_plate)
    elif action == 'OUT':
        if l_plate in car_lot:
            car_lot.remove(l_plate)

if not car_lot:
    print('Parking Lot is Empty')
else:
    [print(l_plate) for l_plate in car_lot]