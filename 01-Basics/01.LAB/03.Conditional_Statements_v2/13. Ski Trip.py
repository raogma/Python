days = int(input())
room = input()
rating = input()

single = 18 * (days - 1)
apartment = 25 * (days - 1)
president_apartment = 35 * (days - 1)

if room == "room for one person":
    if rating == "positive":
            print(f"{single + 0.25 * single:.2f}")
    elif rating == "negative":
            print(f"{single - 0.1 * single:.2f}")

elif room == "apartment":
    if days < 10:
        apartment_v2 = apartment - 0.3 * apartment
        if rating == "positive":
            print(f"{apartment_v2 + 0.25 * apartment_v2:.2f}")
        elif rating == "negative":
            print(f"{apartment_v2 - 0.1 * apartment_v2:.2f}")
    elif 10 <= days <= 15:
        apartment_v2 = apartment - 0.35 * apartment
        if rating == "positive":
            print(f"{apartment_v2 + 0.25 * apartment_v2:.2f}")
        elif rating == "negative":
            print(f"{apartment_v2 - 0.1 * apartment_v2:.2f}")
    elif days > 15:
        apartment_v2 = apartment - 0.5 * apartment
        if rating == "positive":
            print(f"{apartment_v2 + 0.25 * apartment_v2:.2f}")
        elif rating == "negative":
            print(f"{apartment_v2 - 0.1 * apartment_v2:.2f}")

elif room == "president apartment":
    if days < 10:
        president_apartment_v2 = president_apartment - 0.1 * president_apartment
        if rating == "positive":
            print(f"{president_apartment_v2 + 0.25 * president_apartment_v2:.2f}")
        elif rating == "negative":
            print(f"{president_apartment_v2 - 0.1 * president_apartment_v2:.2f}")
    elif 10 <= days <= 15:
        president_apartment_v2 = president_apartment - 0.15 * president_apartment
        if rating == "positive":
            print(f"{president_apartment_v2 + 0.25 * president_apartment_v2:.2f}")
        elif rating == "negative":
            print(f"{president_apartment_v2 - 0.1 * president_apartment_v2:.2f}")
    elif days > 15:
        president_apartment_v2 = president_apartment - 0.2 * president_apartment
        if rating == "positive":
            print(f"{president_apartment_v2 + 0.25 * president_apartment_v2:.2f}")
        elif rating == "negative":
            print(f"{president_apartment_v2 - 0.1 * president_apartment_v2:.2f}")





