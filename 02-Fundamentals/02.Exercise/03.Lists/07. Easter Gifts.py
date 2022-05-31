gifts_list = input().split()
command = input()

while command != "No Money":
    command_list = command.split()
    if "OutOfStock" in command_list:
        for index in range(len(gifts_list)):
            if gifts_list[index] == command_list[1]:
                gifts_list[index] = "None"
    if "Required" in command_list:
        for index in range(len(gifts_list)):
            if index == int(command_list[2]):
                gifts_list[index] = command_list[1]
    if "JustInCase" in command_list:
        gifts_list[-1] = command_list[1]

    command = input()

for element in gifts_list:
    if element != "None":
        print(element, end=" ")
