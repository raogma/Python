wagons = int(input())
train = [0] * wagons

while True:
    command = input()
    if command == "End":
        break

    tokens = command.split(' ')
    type = tokens[0]
    people = int(tokens[-1])
    index = int(tokens[1])
    if type == 'add':
        train[-1] += int(people)
    elif type == 'insert':
        if index >= len(train):
            print("Invalid Operation")
        train[index] += int(people)
    elif type == 'leave':
        if index >= len(train):
            print("Invalid Operation")
        if int(people) <= train[index]:
            train[index] -= int(people)
        else:
            print("Invalid Operation")
print(train)