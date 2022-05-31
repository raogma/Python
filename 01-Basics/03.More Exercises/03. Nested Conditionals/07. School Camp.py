season = input()
group = input()
num_of_students = int(input())
num_of_nights = int(input())

price_per_night = 0
sport = 0
if group == "boys" or group == "girls":
    if season == "Winter":
        price_per_night = 9.6
        if group == "boys":
            sport = "Judo"
        elif group == "girls":
            sport = "Gymnastics"
    elif season == "Spring":
        price_per_night = 7.2
        if group == "boys":
            sport = "Tennis"
        elif group == "girls":
            sport = "Athletics"
    elif season == "Summer":
        price_per_night = 15
        if group == "boys":
            sport = "Football"
        elif group == "girls":
            sport = "Volleyball"

elif group == "mixed":
    if season == "Winter":
        price_per_night = 10
        sport = "Ski"
    elif season == "Spring":
        price_per_night = 9.5
        sport = "Cycling"
    elif season == "Summer":
        price_per_night = 20
        sport = "Swimming"

total_price = price_per_night * num_of_nights * num_of_students

if num_of_students >= 50:
    total_price *= 0.5
elif 20 <= num_of_students < 50:
    total_price *= 0.85
elif 10 <= num_of_students < 20:
    total_price *= 0.95

print(f"{sport} {total_price:.2f} lv.")