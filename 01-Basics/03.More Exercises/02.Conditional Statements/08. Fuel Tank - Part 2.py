fuel_type = input()
quantity_fuel = float(input())
discount_card = input()

price_per_ltr = 0

if fuel_type == "Gasoline":
    price_per_ltr = 2.22
    if discount_card == "Yes":
        price_per_ltr -= 0.18

elif fuel_type == "Diesel":
    price_per_ltr = 2.33
    if discount_card == "Yes":
        price_per_ltr -= 0.12

elif fuel_type == "Gas":
    price_per_ltr = 0.93
    if discount_card == "Yes":
        price_per_ltr -= 0.08

if 20 <= quantity_fuel <= 25:
    price_per_ltr *= 0.92
elif quantity_fuel > 25:
    price_per_ltr *= 0.9

total_price = price_per_ltr * quantity_fuel

print(f"{total_price:.2f} lv.")