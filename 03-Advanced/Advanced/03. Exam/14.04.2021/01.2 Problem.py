from collections import deque

orders = deque(x for x in list(map(int, input().split(', '))) if 0 < x <= 10)
employees = deque(map(int, input().split(', ')))

pizzas_counter = 0
while orders and employees:
    pizza = orders.popleft()
    employee = employees.pop()
    if pizza <= employee:
        pizzas_counter += pizza
    else:
        pizza -= employee
        orders.appendleft(pizza)
        pizzas_counter += employee

if not orders:
    print(f'All orders are successfully completed!\nTotal pizzas made: {pizzas_counter}\n'
          f'Employees: {", ".join(list(map(str, employees)))}')
else:
    print(f'Not all orders are completed.\nOrders left: {", ".join(list(map(str, orders)))}')
