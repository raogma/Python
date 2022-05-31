from sys import maxsize

num_of_cakes = int(input())
total_points = 0
max_points = -maxsize
winner = ""

for cake in range(1, num_of_cakes + 1):
    cooker_name = input()
    points = input()
    while points != "Stop":
        total_points += int(points)
        points = input()
    print(f"{cooker_name} has {total_points} points.")
    if total_points > max_points:
        max_points = total_points
        winner = cooker_name
        print(f"{winner} is the new number 1!")
    total_points = 0

print(f"{winner} won competition with {max_points} points!")