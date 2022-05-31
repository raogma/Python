days = int(input())
men = int(input())

number_of_cakes = int(input())
number_of_waffles = int(input())
number_of_pancakes = int(input())

cake = 45
waffle = 5.8
pancake = 3.2

total_sum = (cake * number_of_cakes + waffle * number_of_waffles + pancake * number_of_pancakes) * days * men

costs = total_sum / 8
charity_sum = total_sum - costs

print(charity_sum)