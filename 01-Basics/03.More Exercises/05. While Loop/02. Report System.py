needed_money = int(input())
command = input()
cash_transactions = 0
cash_sum = 0
card_transactions = 0
card_sum = 0
counter = 0

while command != "End":
    product = int(command)
    counter += 1
    if counter % 2 != 0:    # 1. В брой
        if product > 100:
            print("Error in transaction!")
        else:
            cash_transactions += 1
            cash_sum += product
            needed_money -= product
            print("Product sold!")
    else:                   # 2. С карта
        if product < 10:
            print("Error in transaction!")
        else:
            card_transactions += 1
            card_sum += product
            needed_money -= product
            print("Product sold!")

    if needed_money <= 0:
        print(f"Average CS: {cash_sum / cash_transactions:.2f}")
        print(f"Average CC: {card_sum / card_transactions:.2f}")
        break
    command = input()
else:
    print("Failed to collect required money for charity.")