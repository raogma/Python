width = int(input())
length = int(input())
height = int(input())

volume = width * length * height

while volume >= 0:
    boxes = input()
    if boxes == "Done":
        print(f"{abs(volume)} Cubic meters left.")
        break
    else:
        volume -= int(boxes)
else:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")