x = float(input()) #height_of_house
y = float(input()) #length_of_sidewall
h = float(input()) #height_of_roof

front_wall = x * x - 2.4
back_wall = x * x
side_wall = x * y - 1.5 * 1.5

area_house = front_wall + back_wall + 2 * side_wall
area_roof = x * y * 2 + x * h

green_dye = area_house / 3.4
red_dye = area_roof / 4.3

print(f"{green_dye:.2f}")
print(f"{red_dye:.2f}")