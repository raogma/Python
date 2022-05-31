from copy import deepcopy

items = input()
budget = float(input())
old_budget = deepcopy(budget)

items_list = items.split("|")

total_money = 0

for item in items_list:
    element = item.split("->")
    type = element[0]
    price = float(element[1])
    if price > budget:
        continue
    if (type == "Clothes" and price <= 50) or (type == "Shoes" and price <= 35) or (type == "Accessories" and price <= 20.50):
        budget -= price
        price *= 1.4
        print(f"{price:.2f}", end=" ")
        total_money += round(price, 2)
print()

profit = abs(total_money + budget - old_budget)
print(f"Profit: {profit:.2f}")

if total_money + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
