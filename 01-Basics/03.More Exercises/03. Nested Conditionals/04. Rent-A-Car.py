budget = float(input())
season = input()

price = 0
type_car = 0

if budget <= 100:
    print("Economy class")
    if season == "Summer":
        type_car = "Cabrio"
        price = 0.35 * budget
    elif season == "Winter":
        type_car = "Jeep"
        price = 0.65 * budget
elif 100 < budget <= 500:
    print("Compact class")
    if season == "Summer":
        type_car = "Cabrio"
        price = 0.45 * budget
    elif season == "Winter":
        type_car = "Jeep"
        price = 0.8 * budget
elif budget > 500:
    print("Luxury class")
    type_car = "Jeep"
    price = 0.9 * budget

print(f"{type_car} - {price:.2f}")