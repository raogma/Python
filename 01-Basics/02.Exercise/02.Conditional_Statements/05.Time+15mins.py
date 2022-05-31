hrs = int(input())
minutes = int(input())

current_time = hrs * 60 + minutes
time_ahead = current_time + 15

time_ahead_hrs = time_ahead // 60

if time_ahead_hrs > 23:
    time_ahead_hrs_v2 = time_ahead_hrs - 24
    time_ahead_mins = time_ahead % 60

    if time_ahead_mins <= 9:
        print(f"{time_ahead_hrs_v2}:0{time_ahead_mins}")
    else:
        print(f"{time_ahead_hrs_v2}:{time_ahead_mins}")

else:

    time_ahead_mins = time_ahead % 60

    if time_ahead_mins <=9:
        print(f"{time_ahead_hrs}:0{time_ahead_mins}")
    else:
        print(f"{time_ahead_hrs}:{time_ahead_mins}")