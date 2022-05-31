type_fuel = input()
fuel_left = float(input())

if type_fuel == "Diesel":
    if fuel_left >= 25:
        print(f"You have enough {type_fuel}.")
    elif fuel_left < 25:
        print(f"Fill your tank with {type_fuel}!")

elif type_fuel == "Gasoline":
    if fuel_left >= 25:
        print(f"You have enough {type_fuel}.")
    elif fuel_left < 25:
        print(f"Fill your tank with {type_fuel}!")

elif type_fuel == "Gas":
    if fuel_left >= 25:
        print(f"You have enough {type_fuel}.")
    elif fuel_left < 25:
        print(f"Fill your tank with {type_fuel}!")

else:
    print("Invalid fuel!")
