product = input()
town = input()
quantity = float(input())

if town == "Sofia":
    if product == "coffee":
        print(0.5 * quantity)
    elif product == "water":
        print(0.8 * quantity)
    elif product == "beer":
        print(1.2 * quantity)
    elif product == "sweets":
        print(1.45 * quantity)
    elif product == "peanuts":
        print(1.6 * quantity)
elif town == "Plovdiv":
    if product == "coffee":
        print(0.4 * quantity)
    elif product == "water":
        print(0.7 * quantity)
    elif product == "beer":
        print(1.15 * quantity)
    elif product == "sweets":
        print(1.30 * quantity)
    elif product == "peanuts":
        print(1.5 * quantity)
elif town == "Varna":
    if product == "coffee":
        print(0.45 * quantity)
    elif product == "water":
        print(0.7 * quantity)
    elif product == "beer":
        print(1.10 * quantity)
    elif product == "sweets":
        print(1.35 * quantity)
    elif product == "peanuts":
        print(1.55 * quantity)