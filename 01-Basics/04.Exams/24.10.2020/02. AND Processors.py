needed_CPUs = int(input())
workers = int(input())
days = int(input())

hrs_per_CPU = 3
hrs_per_day = 8
CPU_price = 110.1

total_hrs = days * hrs_per_day * workers
total_CPUs = int(total_hrs / hrs_per_CPU)
total_price = total_CPUs * CPU_price
needed_profit = needed_CPUs * CPU_price
difference = abs(total_price - needed_profit)

if total_price >= needed_profit:
    print(f"Profit: -> {difference:.2f} BGN")
else:
    print(f"Losses: -> {difference:.2f} BGN")
