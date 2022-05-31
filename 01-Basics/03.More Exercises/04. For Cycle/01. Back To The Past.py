inherited_money = float(input())
death_year = int(input())
age = 17
for years in range(1800, death_year + 1):
    age += 1
    if years % 2 == 0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + 50 * age

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")