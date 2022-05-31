record_time = float(input())
distance = float(input())
time_4_1m = float(input())

time = time_4_1m * distance

parts_distance = distance // 15
#// - от у-вието да се закръгли.

time_resistance = parts_distance * 12.5

total_time = time + time_resistance

difference = abs(total_time - record_time)


if total_time < record_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")