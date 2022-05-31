clients = int(input())
back = 0
chest = 0
legs = 0
abs = 0
pshake = 0
pbar = 0

for client in range(1, clients + 1):
    activity = input()
    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs += 1
    elif activity == "Protein shake":
        pshake += 1
    elif activity == "Protein bar":
        pbar += 1

training_clients = back + chest + legs + abs
non_training_clients = pshake + pbar
perc_training_clients = training_clients * 100 / clients
perc_non_training_clients = non_training_clients * 100 / clients


print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{pshake} - protein shake")
print(f"{pbar} - protein bar")
print(f"{perc_training_clients:.2f}% - work out")
print(f"{perc_non_training_clients:.2f}% - protein")
