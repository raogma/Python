time_1secs = int(input())
time2_secs = int(input())
time3_secs = int(input())

total_time_secs = time_1secs + time2_secs + time3_secs
total_time_mins = total_time_secs // 60
total_time_secs = total_time_secs % 60
#35+45+44 == 124s
#124 // 60 == 2
#124 % 60 == 4
if total_time_secs <= 9:
    print(f"{total_time_mins}:0{total_time_secs}")
else:
    print(f"{total_time_mins}:{total_time_secs}")



