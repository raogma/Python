from sys import exit
data = ['days', 'budget', 'people', 'fuel_per_k', 'food_per_p', 'room_per_p']
info = {data[i]: float(input()) for i in range(len(data))}

hotel_expenses = info['room_per_p'] * info['people'] * info['days']
if info['people'] > 10:
    hotel_expenses *= 0.75
food_expenses = info['food_per_p'] * info['people'] * info['days']
current_expenses = food_expenses + hotel_expenses

for i in range(1, int(info['days']) + 1):
    kmeters_per_day = float(input())
    current_expenses += kmeters_per_day * info['fuel_per_k']
    if i % 3 == 0 or i % 5 == 0:
        current_expenses += 0.40 * current_expenses
    elif i % 7 == 0:
        current_expenses -= current_expenses / info['people']
    if current_expenses > info['budget']:
        print(f'Not enough money to continue the trip. You need {abs(info["budget"] - current_expenses):.2f}$ more.')
        exit(0)

print(f'You have reached the destination. You have {abs(current_expenses - info["budget"]):.2f}$ budget left.')
