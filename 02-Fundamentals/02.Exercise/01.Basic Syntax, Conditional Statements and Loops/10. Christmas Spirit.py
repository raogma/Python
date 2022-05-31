quantity = int(input())
days = int(input())

Ornament = 2
Skirt = 5
Garlands = 3
Lights = 15
spirit = 0
budget = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        spirit += 5
        budget += Ornament * quantity

    if day % 3 == 0:
        spirit += 13
        budget += (Garlands + Skirt) * quantity

    if day % 5 == 0:
        spirit += 17
        budget += Lights * quantity

    if day % 3 == 0 and day % 5 == 0:
        spirit += 30

    if day % 10 == 0:
        spirit -= 20
        budget += Skirt + Garlands + Lights
        if day == days:
            spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
