needed_money = float(input())
current_money = float(input())
spend_counter = 0
days_counter = 0

while current_money < needed_money:
    action = input()
    payment = float(input())
    days_counter += 1
    if action == "spend":
        current_money -= payment
        spend_counter += 1
        if payment > current_money:
            current_money = 0
        if spend_counter == 5:
            print("You can't save the money.")
            print(days_counter)
            break
    elif action == "save":
        current_money += payment
        spend_counter = 0
else:
    print(f"You saved the money for {days_counter} days.")