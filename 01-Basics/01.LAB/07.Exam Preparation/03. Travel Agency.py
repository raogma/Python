from sys import exit

town = input()
packet_type = input()
VIP = input()
days = int(input())

if days <= 0:
    print("Days must be positive number!")
    exit(0)
if days > 7:
    days -= 1

price = 0

if town == "Bansko" or town == "Borovets":
    if packet_type == "withEquipment":
        price = 100
        if VIP == "yes":
            price *= 0.9
    elif packet_type == "noEquipment":
        price = 80
        if VIP == "yes":
            price *= 0.95
    else:
        print("Invalid input!")
        exit(0)

elif town == "Varna" or town == "Burgas":
    if packet_type == "withBreakfast":
        price = 130
        if VIP == "yes":
            price *= 0.88
    elif packet_type == "noBreakfast":
        price = 100
        if VIP == "yes":
            price *= 0.93
    else:
        print("Invalid input!")
        exit(0)
else:
    print("Invalid input!")
    exit(0)

print(f"The price is {price * days:.2f}lv! Have a nice time!")
