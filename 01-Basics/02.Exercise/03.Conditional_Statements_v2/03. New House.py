flower = input()
number = int(input())
budget = int(input())

total_price = 0

if flower == "Roses" and number > 80:
    total_price = number * 5 - 0.1 * number * 5
    if budget >= total_price:
        print(f"Hey, you have a great garden with {number} {flower} and {budget - total_price:.2f} leva left.")
    else:
        print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
elif flower == "Roses" and number <= 80:
    total_price = number * 5
    if budget >= total_price:
        print(f"Hey, you have a great garden with {number} {flower} and {budget - total_price:.2f} leva left.")
    else:
        print(f"Not enough money, you need {total_price - budget:.2f} leva more.")

elif flower == "Dahlias" and number > 90:
    total_price = number * 3.8 - 0.15 * number * 3.8
    if budget >= total_price:
        print(f"Hey, you have a great garden with {number} {flower} and {budget - total_price:.2f} leva left.")
    else:
        print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
elif flower == "Dahlias" and number <= 90:
    total_price = number * 3.8
    if budget >= total_price:
        print(f"Hey, you have a great garden with {number} {flower} and {budget - total_price:.2f} leva left.")
    else:
        print(f"Not enough money, you need {total_price - budget:.2f} leva more.")

elif flower == "Tulips" and number > 80:
    total_price = number * 2.8 - 0.15 * number * 2.8
    if budget >= total_price:
        print(f"Hey, you have a great garden with {number} {flower} and {budget - total_price:.2f} leva left.")
    else:
        print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
elif flower == "Tulips" and number <= 80:
    total_price = number * 2.8
    if budget >= total_price:
        print(f"Hey, you have a great garden with {number} {flower} and {budget - total_price:.2f} leva left.")
    else:
        print(f"Not enough money, you need {total_price - budget} leva more.")

elif flower == "Narcissus" and number < 120:
    total_price = number * 3 + 0.15 * number * 3
    if budget >= total_price:
        print(f"Hey, you have a great garden with {number} {flower} and {budget - total_price:.2f} leva left.")
    else:
        print(f"Not enough money, you need {total_price - budget} leva more.")
elif flower == "Narcissus" and number >= 120:
    total_price = number * 3
    if budget >= total_price:
        print(f"Hey, you have a great garden with {number} {flower} and {budget - total_price:.2f} leva left.")
    else:
        print(f"Not enough money, you need {total_price - budget:.2f} leva more.")

elif flower == "Gladiolus" and number < 80:
    total_price = number * 2.5 + 0.2 * number * 2.5
    if budget >= total_price:
        print(f"Hey, you have a great garden with {number} {flower} and {budget - total_price:.2f} leva left.")
    else:
        print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
elif flower == "Gladiolus" and number >= 80:
    total_price = number * 2.5
    if budget >= total_price:
        print(f"Hey, you have a great garden with {number} {flower} and {budget - total_price:.2f} leva left.")
    else:
        print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
