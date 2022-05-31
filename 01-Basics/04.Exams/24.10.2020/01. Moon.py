from math import ceil
V = float(input())
needed_fuel_per100 = float(input())

S = 384400 * 2
total_fuel = S * needed_fuel_per100 / 100

t = S / V + 3

print(ceil(t))
print(int(total_fuel))