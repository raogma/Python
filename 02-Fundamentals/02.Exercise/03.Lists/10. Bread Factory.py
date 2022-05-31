events = input().split("|")

initial_energy = 100
energy = 100
exceeded = 0
coins = 100
isFailed = False

for event in events:
    element = event.split("-")
    type = element[0]
    value = int(element[1])
    if type == "rest":
        energy += value
        if energy > initial_energy:
            exceeded = energy - initial_energy
            value -= exceeded
            energy -= exceeded
        print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")

    elif type == "order":
        energy -= 30
        if energy < 0:
            energy += 30
            energy += 50
            print("You had to rest!")
            continue
        else:
            coins += value
            print(f"You earned {value} coins.")

    else:
        coins -= value
        if coins > 0:
            print(f"You bought {type}.")
        else:
            print(f"Closed! Cannot afford {type}.")
            isFailed = True
            break

if not isFailed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")