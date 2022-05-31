width = int(input())
length = int(input())

total_pieces = width * length
command = input()

while command != "STOP":
    pieces = int(command)
    total_pieces -= pieces
    if total_pieces < 0:
        print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
        break #EOF mistake
    command = input()
else:
    print(f"{abs(total_pieces)} pieces are left.")
