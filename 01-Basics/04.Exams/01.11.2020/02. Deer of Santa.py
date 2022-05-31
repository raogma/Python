from math import ceil
from math import floor

days = int(input())
total_food_kgs = int(input())
first_deer_per_day = float(input())
second_deer_per_day = float(input())
third_deer_per_day = float(input())

needed_food = days * (first_deer_per_day + second_deer_per_day + third_deer_per_day)
difference = abs(needed_food - total_food_kgs)

if needed_food <= total_food_kgs:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")