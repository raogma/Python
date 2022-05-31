budget = int(input())
season = input()
fishermen = int(input())

price = 0
price_v2 = 10

if fishermen <=6:
    if season == "Spring":
        price = 3000 - 0.1 * 3000
        if fishermen % 2 == 0:
            price_v2 = price - 0.05 * price
            if budget >= price_v2:
                print(f"Yes! You have {budget - price_v2:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price_v2 - budget:.2f} leva.")
        else:
            if budget >= price:
                print(f"Yes! You have {budget - price:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price - budget:.2f} leva.")

    elif season == "Summer":
        price = 4200 - 0.1 * 4200
        if fishermen % 2 == 0:
            price_v2 = price - 0.05 * price
            if budget >= price_v2:
                print(f"Yes! You have {budget - price_v2:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price_v2 - budget:.2f} leva.")
        else:
            if budget >= price:
                print(f"Yes! You have {budget - price:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price - budget:.2f} leva.")

    elif season == "Winter":
        price = 2600 - 0.1 * 2600
        if fishermen % 2 == 0:
            price_v2 = price - 0.05 * price
            if budget >= price_v2:
                print(f"Yes! You have {budget - price_v2:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price_v2 - budget:.2f} leva.")
        else:
            if budget >= price:
                print(f"Yes! You have {budget - price:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price - budget:.2f} leva.")

    elif season == "Autumn":
        price = 4200 - 0.1 * 4200
        if budget >= price:
            print(f"Yes! You have {budget - price:.2f} leva left.")
        else:
            print(f"Not enough money! You need {price - budget:.2f} leva.")

elif 7 <= fishermen <= 11:
    if season == "Spring":
        price = 3000 - 0.15 * 3000
        if fishermen % 2 == 0:
            price_v2 = price - 0.05 * price
            if budget >= price_v2:
                print(f"Yes! You have {budget - price_v2:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price_v2 - budget:.2f} leva.")
        else:
            if budget >= price:
                print(f"Yes! You have {budget - price:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price - budget:.2f} leva.")

    elif season == "Summer":
        price = 4200 - 0.15 * 4200
        if fishermen % 2 == 0:
            price_v2 = price - 0.05 * price
            if budget >= price_v2:
                print(f"Yes! You have {budget - price_v2:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price_v2 - budget:.2f} leva.")
        else:
            if budget >= price:
                print(f"Yes! You have {budget - price:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price - budget:.2f} leva.")

    elif season == "Winter":
        price = 2600 - 0.15 * 2600
        if fishermen % 2 == 0:
            price_v2 = price - 0.05 * price
            if budget >= price_v2:
                print(f"Yes! You have {budget - price_v2:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price_v2 - budget:.2f} leva.")
        else:
            if budget >= price:
                print(f"Yes! You have {budget - price:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price - budget:.2f} leva.")

    elif season == "Autumn":
        price = 4200 - 0.15 * 4200
        if budget >= price:
            print(f"Yes! You have {budget - price:.2f} leva left.")
        else:
            print(f"Not enough money! You need {price - budget:.2f} leva.")

elif fishermen >= 12:
    if season == "Spring":
        price = 3000 - 0.25 * 3000
        if fishermen % 2 == 0:
            price_v2 = price - 0.05 * price
            if budget >= price_v2:
                print(f"Yes! You have {budget - price_v2:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price_v2 - budget:.2f} leva.")
        else:
            if budget >= price:
                print(f"Yes! You have {budget - price:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price - budget:.2f} leva.")

    elif season == "Summer":
        price = 4200 - 0.25 * 4200
        if fishermen % 2 == 0:
            price_v2 = price - 0.05 * price
            if budget >= price_v2:
                print(f"Yes! You have {budget - price_v2:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price_v2 - budget:.2f} leva.")
        else:
            if budget >= price:
                print(f"Yes! You have {budget - price:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price - budget:.2f} leva.")

    elif season == "Winter":
        price = 2600 - 0.25 * 2600
        if fishermen % 2 == 0:
            price_v2 = price - 0.05 * price
            if budget >= price_v2:
                print(f"Yes! You have {budget - price_v2:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price_v2 - budget:.2f} leva.")
        else:
            if budget >= price:
                print(f"Yes! You have {budget - price:.2f} leva left.")
            else:
                print(f"Not enough money! You need {price - budget:.2f} leva.")

    elif season == "Autumn":
        price = 4200 - 0.25 * 4200
        if budget >= price:
            print(f"Yes! You have {budget - price:.2f} leva left.")
        else:
            print(f"Not enough money! You need {price - budget:.2f} leva.")
