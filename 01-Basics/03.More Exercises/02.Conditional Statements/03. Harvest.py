from math import ceil

area = int(input())
kg_grape_per_sq_m = float(input())
needed_litres = int(input())
workers = int(input())

total_kg_grape = kg_grape_per_sq_m * area
total_kgs_wine = total_kg_grape * 0.4
total_ls_wine = total_kgs_wine / 2.5
difference = abs(needed_litres - total_ls_wine)
wine_per_worker = difference / workers

if total_ls_wine < needed_litres:
    print(f"It will be a tough winter! More {int(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {int(total_ls_wine)} liters.")
    print(f"{ceil(difference)} liters left -> {ceil(wine_per_worker)} liters per person.")
