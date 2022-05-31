width = int(input())
length = int(input())
height = int(input())

volume = width * length * height
boxes = input()

while boxes != "Done":
    volume -= int(boxes)
    if volume <= 0:
        print(f"No more free space! You need {abs(volume)} Cubic meters more.")
        break
    boxes = input()
else:
    print(f"{abs(volume)} Cubic meters left.")