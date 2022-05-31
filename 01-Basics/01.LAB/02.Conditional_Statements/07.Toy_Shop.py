holiday = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.

total_money = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2
discount_prize = total_money - 0.25 * total_money

lease_total_money = total_money - 0.1 * total_money
lease_discount_prize = discount_prize - 0.1 * discount_prize

number_of_toys = puzzles + dolls + bears + minions + trucks

total_money_left = lease_total_money - holiday
discount_money_left = lease_discount_prize - holiday


if number_of_toys >= 50:
    if lease_discount_prize - holiday >= 0:
        print(f"Yes! {discount_money_left:.2f} lv left.")
    else:
        print(f"Not enough money! {abs(discount_money_left):.2f} lv needed.")

else:
    if lease_total_money - holiday >= 0:
        print(f"Yes! {total_money_left:.2f} lv left.")
    else:
        print(f"Not enough money! {abs(total_money_left):.2f} lv needed.")

