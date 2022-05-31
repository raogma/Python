needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
hrs_work = int(input())

price = 1.5 * (needed_nylon + 2) + needed_paint * 14.5 * 1.1 + needed_thinner * 5 + 0.4
work = hrs_work * 0.3 * price
total_price = price + work
print(f"Total expenses: {total_price:.2f} lv.")