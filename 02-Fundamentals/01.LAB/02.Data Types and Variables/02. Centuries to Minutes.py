centuries = int(input())

yrs = centuries * 100
days = int(yrs * 365.2422)
hrs = days * 24
mins = hrs * 60

print(f"{centuries} centuries = {yrs} years = {days} days = {hrs} hours = {mins} minutes")
