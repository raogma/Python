dancers = int(input())
points = float(input())
season = input()
location = input()

price = 0

if location == "Bulgaria":
    price = dancers * points
    if season == "summer":
       price *= 0.95
    elif season == "winter":
        price *= 0.92
elif location == "Abroad":
    price = dancers * points * 1.5
    if season == "summer":
        price *= 0.90
    elif season == "winter":
        price *= 0.85

charity = price - 0.75 * price
price_per_dancer = charity / dancers

print(f"Charity - {0.75 * price:.2f}")
print(f"Money per dancer - {price_per_dancer:.2f}")