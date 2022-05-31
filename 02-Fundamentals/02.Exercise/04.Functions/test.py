from math import floor

text = input()
list = text.split(", ")
for element in list:
    if int(element) < 0:
        element = int(element) * -1
        element = str(element)
    first_half = " "
    second_half = " "
    for sub_element in range(0, round(len(element) / 2)):
        first_half += element[sub_element]
    for sub_element in range(len(element) - 1, floor(len(element) / 2) - 1, -1):
        second_half += element[sub_element]
    if first_half == second_half:
        print("True")
    else:
        print("False")