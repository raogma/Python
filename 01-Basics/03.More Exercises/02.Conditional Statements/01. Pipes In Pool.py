pool = int(input())
p1_per_hour = int(input()) #p1 = pipe1
p2_per_hour = int(input()) #p2 = pipe2
hours = float(input())

p1_total = p1_per_hour * hours
p2_total = p2_per_hour * hours
filled_water = p1_total + p2_total

#x = percent_filled_water
#pool * x / 100 = filled_water
# x = filled_water * 100 / pool

perc_filled_water = filled_water * 100 / pool

#y = percent_p1_total
# filled_water * y / 100 = p1
# y = p1 * 100 / filled_water

perc_p1_total = p1_total * 100 / filled_water
perc_p2_total = p2_total * 100 / filled_water

difference = abs(pool - filled_water)

if filled_water <= pool:
    print(f"The pool is {perc_filled_water}% full. Pipe 1: {perc_p1_total}%. Pipe 2: {perc_p2_total}%.")
else:
    print(f"For {hours} hours the pool overflows with {difference} liters.")
