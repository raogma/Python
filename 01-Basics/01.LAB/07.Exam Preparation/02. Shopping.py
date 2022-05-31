budget = float(input())
GPU = int(input())
CPU = int(input())
RAM = int(input())

price_GPU = 250 * GPU
price_CPU = 0.35 * price_GPU * CPU
price_RAM = 0.1 * price_GPU * RAM
price = price_CPU + price_GPU + price_RAM

if GPU > CPU:
    price *= 0.85

difference = abs(budget - price)

if budget < price:
    print(f"Not enough money! You need {difference:.2f} leva more!")
else:
    print(f"You have {difference:.2f} leva left!")