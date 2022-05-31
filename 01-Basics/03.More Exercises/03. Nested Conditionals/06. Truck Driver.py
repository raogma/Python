season = input()
kms_per_month = float(input())

price_per_km = 0

if kms_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.9
    elif season == "Winter":
        price_per_km = 1.05

elif 5000 < kms_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.1
    elif season == "Winter":
        price_per_km = 1.25

elif 10000 < kms_per_month <= 20000:
    price_per_km = 1.45

total_price = price_per_km * kms_per_month * 4
total_price *= 0.9 #taxes

print(f"{total_price:.2f}")