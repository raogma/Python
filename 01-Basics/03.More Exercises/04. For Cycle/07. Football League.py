stadium_capacity = int(input())
fans = int(input())
fans_A = 0
fans_B = 0
fans_V = 0
fans_G = 0

for fans in range(1, fans + 1):
    sector = input()
    if sector == "A":
        fans_A += 1
    elif sector == "B":
        fans_B += 1
    elif sector == "V":
        fans_V += 1
    elif sector == "G":
        fans_G += 1

perc_fans_A = fans_A * 100 / fans
perc_fans_B = fans_B * 100 / fans
perc_fans_V = fans_V * 100 / fans
perc_fans_G = fans_G * 100 / fans
perc_fans = fans * 100 / stadium_capacity

print(f"{perc_fans_A:.2f}%")
print(f"{perc_fans_B:.2f}%")
print(f"{perc_fans_V:.2f}%")
print(f"{perc_fans_G:.2f}%")
print(f"{perc_fans:.2f}%")