num_chrysanthemums = int(input())
num_roses = int(input())
num_tulips = int(input())
season = input()
holiday = input()

price_chrysanthemums = 0
price_roses = 0
price_tulips = 0

if season == "Spring" or season == "Summer":
    price_chrysanthemums = 2
    price_roses = 4.1
    price_tulips = 2.5
elif season == "Autumn" or season == "Winter":
    price_chrysanthemums = 3.75
    price_roses = 4.5
    price_tulips = 4.15

total_num_flowers = num_chrysanthemums + num_roses + num_tulips
total_price = num_chrysanthemums * price_chrysanthemums + num_roses * price_roses\
    + num_tulips * price_tulips

if holiday == "Y":
    total_price *= 1.15

if num_tulips > 7 and season == "Spring":
    total_price *= 0.95
elif num_roses >= 10 and season == "Winter":
    total_price *= 0.9

if total_num_flowers > 20:
    total_price *= 0.8

total_price += 2

print(f"{total_price:.2f}")

