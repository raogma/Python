fires = input()
water = int(input())

fires_list = fires.split("#")
total_fire = 0
effort = 0
print("Cells:")

for fire in fires_list:
    cell = fire.split(" = ")
    type = cell[0]
    value = int(cell[1])
    if water < value:
        continue
    if (type == "High" and (81 <= value <= 125)) or (type == "Medium" and (51 <= value <= 80)) or (type == "Low" and (1 <= value <= 50)):
        water -= value
        effort += value * 0.25
        total_fire += value
        print(f"- {value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")