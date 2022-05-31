days = int(input())
hrs_per_day = int(input())

price_per_day = 0
total_price = 0

for day in range(1, days + 1):
    for hour in range(1, hrs_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price_per_day += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price_per_day += 1.25
        else:
            price_per_day += 1
    print(f"Day: {day} - {price_per_day:.2f} leva")
    total_price += price_per_day
    price_per_day = 0

print(f"Total: {total_price:.2f} leva")