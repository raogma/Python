from math import ceil

days = int(input())
food_left = int(input())
dog_food_per_day = float(input()) #kgs
cat_food_per_day = float(input()) #kgs
turtle_food_per_day = float(input()) #grs

total_food_per_day = dog_food_per_day + cat_food_per_day + turtle_food_per_day / 1000
food_needed = total_food_per_day * days
difference = abs(food_left - food_needed)

if food_left >= food_needed:
    print(f"{int(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")