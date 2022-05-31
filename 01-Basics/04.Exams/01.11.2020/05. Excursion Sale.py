num_seas = int(input())
num_mountains = int(input())
command = input()

total_price = 0
sea_price = 680
mountain_price = 499

while command != "Stop":
    if command == "sea":
        num_seas -= 1
        if num_seas >= 0:
            total_price += sea_price
        else:
            total_price += 0
    elif command == "mountain":
        num_mountains -= 1
        if num_mountains >= 0:
            total_price += mountain_price
        else:
            total_price += 0

    if num_seas <= 0 and num_mountains <= 0:
        print(f" Good job! Everything is sold.")
        break
    command = input()

print(f"Profit: {total_price} leva.")