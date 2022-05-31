payment = (input())

sum = 0

while payment != "NoMoreMoney":
    if float(payment) < 0:
        print("Invalid operation!")
        break
    sum += float(payment)
    print(f"Increase: {float(payment):.2f}")
    payment = input()

print(f"Total: {sum:.2f}")