needed_hours_4_project = int(input())
days = int(input())
workers_off_duty = int(input())

#10% for training
training = 0.1 * days
days_available = days - training
hours_available = days_available * 8
bonus_hours = workers_off_duty * 2 * days
total_hours_available = int(hours_available) + int(bonus_hours)
difference = abs(needed_hours_4_project - total_hours_available)

if total_hours_available >= needed_hours_4_project:
    print(f"Yes!{int(difference)} hours left.")
else:
    print(f"Not enough time!{int(difference)} hours needed.")
