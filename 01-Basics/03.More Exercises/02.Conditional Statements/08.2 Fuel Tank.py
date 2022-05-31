type_fuel = input()
fuel_left = float(input())

if type_fuel == "Diesel":
    if fuel_left >= 25:
        print(f"You have enough diesel.")
    elif fuel_left < 25:
        print(f"Fill your tank with diesel!")

elif type_fuel == "Gasoline":
    if fuel_left >= 25:
        print(f"You have enough gasoline.")
    elif fuel_left < 25:
        print(f"Fill your tank with gasoline!")

elif type_fuel == "Gas":
    if fuel_left >= 25:
        print(f"You have enough gas.")
    elif fuel_left < 25:
        print(f"Fill your tank with gas!")

else:
    print("Invalid fuel!")
