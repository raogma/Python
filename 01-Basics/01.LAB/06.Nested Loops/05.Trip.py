location = input()

while location != "End":
    needed_money = float(input())
    total_savings = 0
    while total_savings < needed_money:
        savings = float(input())
        total_savings += savings
        if total_savings >= needed_money:
            print(f"Going to {location}!")
            location = input()
