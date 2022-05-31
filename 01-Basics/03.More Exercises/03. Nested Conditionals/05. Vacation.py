budget = float(input())
season = input()

price = 0
type = 0
location = 0

if season == "Summer":
    location = "Alaska"
elif season == "Winter":
    location = "Morocco"

if budget <= 1000:
    type = "Camp"
    if season == "Summer":
        price = 0.65 * budget
    elif season == "Winter":
        price = 0.45 * budget

elif 1000 < budget <= 3000:
    type = "Hut"
    if season == "Summer":
        price = 0.8 * budget
    elif season == "Winter":
        price = 0.6 * budget

elif budget > 3000:
    type = "Hotel"
    price = 0.9 * budget

print(f"{location} - {type} - {price:.2f}")