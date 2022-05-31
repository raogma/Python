type = input()
quantity = int(input())
budget = int(input())
#"Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";

price_per_flower = 0

if type == "Roses":
    price_per_flower = 5
    if quantity > 80:
        price_per_flower *= 0.9

elif type == "Dahlias":
    price_per_flower = 3.8
    if quantity > 90:
        price_per_flower *= 0.85

elif type == "Tulips":
    price_per_flower = 2.8
    if quantity > 80:
        price_per_flower *= 0.85

elif type == "Narcissus":
    price_per_flower = 3
    if quantity < 120:
        price_per_flower *= 1.15

elif type == "Gladiolus":
    price_per_flower = 2.5
    if quantity < 80:
        price_per_flower *= 1.2

total_price = quantity * price_per_flower
difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {quantity} {type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")

