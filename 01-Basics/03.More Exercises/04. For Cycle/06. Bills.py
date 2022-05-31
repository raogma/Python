months = int(input())

total_electricity = 0
total = 0
water = 20
internet = 15
others_per_month = 0
others = 0

for months in range(1, months + 1):
    electricity_per_month = float(input())
    others_per_month = (water + internet + electricity_per_month) * 1.2
    others += others_per_month
    total_electricity += electricity_per_month
    total_per_month = electricity_per_month + water + internet + others_per_month
    total += total_per_month

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {water * months:.2f} lv")
print(f"Internet: {internet * months:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {total / months:.2f} lv")