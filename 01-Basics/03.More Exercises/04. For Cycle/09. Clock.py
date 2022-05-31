sum = 0
hrs = 0
mins = 0

while sum < 1440:
    if sum < 60:
        mins = sum
    else:
        hrs = sum // 60
        mins = sum % 60
    print(f"{hrs} : {mins}")
    sum += 1
