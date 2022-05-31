hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

total_mins_exam = hour_exam * 60 + minute_exam
total_min_arrival = hour_arrival * 60 + minute_arrival
total_difference_mins = total_mins_exam - total_min_arrival
hour = abs(total_difference_mins) // 60
minutes = abs(total_difference_mins) % 60

if total_difference_mins < 0:
    print("Late")
    if abs(total_difference_mins) >= 60:
        if abs(minutes) >= 10:
            print(f"{abs(hour)}:{abs(minutes)} hours after the start")
        else:
            print(f"{abs(hour)}:0{abs(minutes)} hours after the start")
    else:
        print(f"{abs(total_difference_mins)} minutes after the start")

elif 0 <= total_difference_mins <= 30:
    if total_difference_mins == 0:
        print("On time")
    else:
        print("On time")
        print(f"{total_difference_mins} minutes before the start")

elif total_difference_mins > 30:
    print("Early")
    if total_difference_mins < 60:
        print(f"{total_difference_mins} minutes before the start")
    else:
        if minutes < 10:
            print(f"{hour}:0{minutes} hours before the start")
        else:
            print(f"{hour}:{minutes} hours before the start")
