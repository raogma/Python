people = int(input())
capacity = int(input())

counter = 0

while people > 0:
    counter += 1
    people -= capacity

print(counter)