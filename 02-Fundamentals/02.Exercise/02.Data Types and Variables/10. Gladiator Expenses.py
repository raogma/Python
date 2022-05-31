lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

price = 0
shield_counter = 0

for lost_fight in range(1, lost_fights + 1):
    if lost_fight % 2 == 0:
        price += helmet_price
    if lost_fight % 3 == 0:
        price += sword_price
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        price += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            price += armor_price
print(f"Gladiator expenses: {price:.2f} aureus")