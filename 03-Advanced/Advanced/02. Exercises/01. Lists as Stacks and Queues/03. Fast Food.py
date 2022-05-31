from collections import deque

quantity_of_food = int(input())
orders = deque(map(lambda x: int(x), input().split()))

print(max(orders))

while orders:
    order = orders.popleft()
    if quantity_of_food - order >= 0:
        quantity_of_food -= order
    else:
        orders.appendleft(order)
        break

if not orders:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join(map(lambda x:str(x), orders))}')
