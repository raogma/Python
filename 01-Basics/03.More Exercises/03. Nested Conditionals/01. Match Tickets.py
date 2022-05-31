budget = float(input())
ticket = input()
num_of_people = int(input())

price_ticket = 0

if ticket == "VIP":
    price_ticket = 499.99
elif ticket == "Normal":
    price_ticket = 249.99

if 1 <= num_of_people <= 4:
    budget *= 0.25
elif 5 <= num_of_people <= 9:
    budget *= 0.4
elif 10 <= num_of_people <= 24:
    budget *= 0.5
elif 25 <= num_of_people <= 49:
    budget *= 0.6
elif num_of_people >= 50:
    budget *= 0.75

total_price = num_of_people * price_ticket
difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")

