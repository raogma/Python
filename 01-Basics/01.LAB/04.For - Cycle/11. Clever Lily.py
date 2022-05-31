age = int(input())
price_washing_machine = float(input())
price_per_toy = int(input())

num_of_toys = 0
money_per_year = 0
total_money = 0

for age in range(1, age + 1):
    if age % 2 != 0:
        num_of_toys += 1
    else:
        money_per_year = money_per_year + 10            #2 -> 10, 4 -> 20, 6 -> 30
        total_money = total_money + money_per_year - 1

saved_money = num_of_toys * price_per_toy + total_money
difference = abs(saved_money - price_washing_machine)

if saved_money >= price_washing_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")