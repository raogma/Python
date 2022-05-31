num_of_loads = int(input())

price_per_ton = 0
price_per_load = 0
total_price = 0
bus_tons = 0
truck_tons = 0
train_tons = 0

for num_of_loads in range(1, num_of_loads + 1):
    tons = float(input())
    if tons <= 3:
        price_per_ton = 200
        bus_tons += tons
    elif tons <= 11:
        price_per_ton = 175
        truck_tons += tons
    elif tons >= 12:
        price_per_ton = 120
        train_tons += tons

    price_per_load = price_per_ton * tons
    total_price += price_per_load

total_tons = bus_tons + truck_tons + train_tons
av_price_per_ton = total_price / total_tons
perc_bus = bus_tons * 100 / total_tons
perc_truck = truck_tons * 100 / total_tons
perc_train = train_tons * 100 / total_tons

print(f"{av_price_per_ton:.2f}")
print(f"{perc_bus:.2f}%")
print(f"{perc_truck:.2f}%")
print(f"{perc_train:.2f}%")
