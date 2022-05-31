month = input()
overnights = int(input())
price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = overnights * 50
    if 7 < overnights <= 14:
        price_studio *= 0.95
    elif overnights > 14:
        price_studio *= 0.7
    price_apartment = overnights * 65
    if overnights > 14:
        price_apartment *= 0.9

elif month == "June" or month == "September":
    price_studio = overnights * 75.2
    if overnights > 14:
        price_studio *= 0.8
    price_apartment = overnights * 68.7
    if overnights > 14:
        price_apartment *= 0.9

elif month == "July" or month == "August":
    price_studio = overnights * 76
    price_apartment = overnights * 77
    if overnights > 14:
        price_apartment *= 0.9

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")