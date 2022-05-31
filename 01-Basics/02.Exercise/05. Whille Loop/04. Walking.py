target = 10000

steps = input()

while steps != "Going home":
    target -= int(steps)
    if target <= 0:
        print("Goal reached! Good job!")
        print(f"{abs(target)} steps over the goal!")
        break
    steps = input()
else:
    steps = input()
    target -= int(steps)
    if target > 0:
        print(f"{abs(target)} more steps to reach goal.")
    else:
        print("Goal reached! Good job!")
        print(f"{abs(target)} steps over the goal!")

