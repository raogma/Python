locations = int(input())

total_gold = 0

for location in range(1, locations + 1):
    needed_extraction_per_day = float(input())
    days = int(input())
    for day in range(1, days + 1):
        gold = float(input())
        total_gold += gold
    average_gold_per_day = total_gold / days
    difference = abs(needed_extraction_per_day - average_gold_per_day)
    if average_gold_per_day >= needed_extraction_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        print(f"You need {difference:.2f} gold.")
    total_gold = 0