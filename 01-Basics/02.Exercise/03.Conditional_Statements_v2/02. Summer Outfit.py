degrees = int(input())
time = input()

outfit = 0
shoes = 0

if time == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

    elif degrees >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

elif time == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

    elif 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

    elif degrees >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

elif time == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")


