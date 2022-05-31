num_juniors = int(input())
num_seniors = int(input())
type_race = input()

price_juniors = 0
price_seniors = 0
num_of_people = num_juniors + num_seniors

if type_race == "trail":
    price_juniors = 5.5
    price_seniors = 7
elif type_race == "cross-country":
    price_juniors = 8
    price_seniors = 9.5
    if num_of_people >= 50:
        price_juniors *= 0.75
        price_seniors *= 0.75

elif type_race == "downhill":
    price_juniors = 12.25
    price_seniors = 13.75
elif type_race == "road":
    price_juniors = 20
    price_seniors = 21.5

total_money = price_juniors * num_juniors + price_seniors * num_seniors
total_money *= 0.95 #for expenses

print(f"{total_money:.2f}")


