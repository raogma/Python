from math import ceil

num_of_magnolias = int(input())
num_of_hyacinths = int(input()) #зюмбюл
num_of_roses = int(input())
num_of_cacti = int(input()) #кактуси
present = float(input())

price_magnolias = 3.25
price_hyacinths = 4
price_roses = 3.50
price_cacti = 8

total_sum = price_magnolias * num_of_magnolias + price_hyacinths * num_of_hyacinths\
    + price_roses * num_of_roses + price_cacti * num_of_cacti
profit = total_sum - 0.05 * total_sum
difference = abs(profit - present)

if profit >= present:
    print(f"She is left with {int(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")


