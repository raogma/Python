days = int(input())
cookers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

total_sum = (cakes * 45 + waffles * 5.8 + pancakes * 3.2) * cookers * days
costs = total_sum / 8
charity_sum = total_sum - costs

print(charity_sum)