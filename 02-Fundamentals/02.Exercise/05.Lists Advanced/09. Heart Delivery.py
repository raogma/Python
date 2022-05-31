neighbourhood = input().split('@')
neighbourhood_nums = list(map(lambda x: int(x), neighbourhood))

length = 0

while True:
    command = input()
    if command == "Love!":
        break
    jump = command.split()
    length += int(jump[1])
    if length > len(neighbourhood_nums) - 1:
        length = 0
    if neighbourhood_nums[length] == 0:
        print(f"Place {length} already had Valentine's day.")
        continue
    else:
        neighbourhood_nums[length] -= 2
        if neighbourhood_nums[length] == 0:
            print(f"Place {length} has Valentine's day.")

print(f"Cupid's last position was {length}.")

failed_list = list(filter(lambda y: y != 0, neighbourhood_nums))

if len(failed_list) == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(failed_list)} places.")
