needed_profit = float(input())
name_of_drinks = input()
price_per_drink = 0
price = 0
total_price = 0
difference = 0

while name_of_drinks != "Party!":
    price_per_drink = len(name_of_drinks)
    num_drinks = int(input())
    price = price_per_drink * num_drinks
    if price % 2 != 0:
        price *= 0.75
    total_price += price
    difference = abs(total_price - needed_profit)
    if total_price >= needed_profit:
        print("Target acquired.")
        print(f"Club income - {total_price:.2f} leva.")
        break
    name_of_drinks = input()
else:
    print(f"We need {difference:.2f} leva more.")
    print(f"Club income - {total_price:.2f} leva.")