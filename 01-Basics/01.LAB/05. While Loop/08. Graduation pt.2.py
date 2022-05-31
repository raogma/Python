name = input()
grade = 1
mistakes = 0
rating_sum = 0

while grade <= 12:
    rating = float(input())
    if rating >= 4:
        grade += 1
    else:
        mistakes += 1
    if mistakes > 1:
        print(f"{name} has been excluded at {grade} grade")
        break
    rating_sum += rating
else:
    average_rating = rating_sum / 12
    print(f"{name} graduated. Average grade: {average_rating:.2f}")
