hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

total_mins_exam = hour_exam * 60 + minute_exam
total_min_arrival = hour_arrival * 60 + minute_arrival
difference_mins = total_mins_exam - total_min_arrival


if difference_mins < 0:
    print("Late")
    if abs(difference_mins) >= 60:
        if abs(difference_mins) % 60 >= 10:
            print(f"{abs(difference_mins) // 60}:{abs(difference_mins) % 60} hours after the start" )
        else:
            print(f"{abs(difference_mins) // 60}:0{abs(difference_mins) % 60} hours after the start" )
    else:
        print(f"{abs(difference_mins)} minutes after the start" )

elif 0 <= difference_mins <= 30:
    if difference_mins == 0:
        print("On time")
    else:
        print("On time")
        print(f"{difference_mins} minutes before the start" )

elif difference_mins > 30:
    print("Early")
    if difference_mins < 60:
        print(f"{difference_mins} minutes before the start" )
    else:
        if difference_mins % 60 < 10:
            print(f"{difference_mins // 60}:0{difference_mins % 60} hours before the start" )
        else:
            print(f"{difference_mins // 60}:{difference_mins % 60} hours before the start" )
