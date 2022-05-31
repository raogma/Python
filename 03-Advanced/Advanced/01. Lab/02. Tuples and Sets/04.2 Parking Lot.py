input_count = int(input())

car_lot = list()

for _ in range(input_count):
    action, l_plate = input().split(', ')
    if action == 'IN':
        if l_plate not in car_lot:
            car_lot.append(l_plate)
    elif action == 'OUT':
        if l_plate in car_lot:
            car_lot.remove(l_plate)

if not car_lot:
    print('Parking Lot is Empty')
else:
    [print(l_plate) for l_plate in car_lot]