deposit = float(input())
months = float(input())
annual_percent = float(input())

final_price = deposit + months * deposit * annual_percent / 100 / 12
print(final_price)
