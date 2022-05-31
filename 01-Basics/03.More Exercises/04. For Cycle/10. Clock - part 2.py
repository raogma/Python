sum = 0
hrs = 0
mins = 0
secs = 0
while sum < 86400:
    if sum < 60:
        secs = sum
    elif sum < 3600:
        mins = sum // 60
        secs = sum % 60
    else:
        hrs = sum // 3600
        mins = sum // 60 % 60
        secs = sum % 60

    print(f"{hrs} : {mins} : {secs}")
    sum += 1


