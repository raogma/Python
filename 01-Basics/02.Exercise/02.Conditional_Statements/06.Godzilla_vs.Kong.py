budget = float(input())
statists = int(input())
clothing_price = float(input())

decor = 0.1 * budget

if statists > 150:
    clothing_price_v2 = clothing_price - 0.1 * clothing_price
    total_price = decor + clothing_price_v2 * statists
    if total_price > budget:
        print(f"Not enough money!")
        print(f"Wingard needs {total_price - budget:.2f} leva more.")
    else:
        print(f"Action!")
        print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")

else:
    total_price = decor + clothing_price * statists
    if total_price > budget:
        print(f"Not enough money!")
        print(f"Wingard needs {total_price - budget:.2f} leva more.")
    else:
        print(f"Action!")
        print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")