numbers_dictionary = {}
isValid = True

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
    except ValueError:
        print('The variable number must be an integer')
        isValid = False
        break
    if number_as_string not in numbers_dictionary:
        numbers_dictionary[number_as_string] = number
    line = input()

if isValid:
    line = input()
    while line != "Remove":
        searched = line
        if searched in numbers_dictionary:
            print(f'\n{numbers_dictionary[searched]}')
        else:
            print('Number does not exist in dictionary')
            isValid = False
            break
        line = input()

    if isValid:
        line = input()
        while line != "End":
            searched = line
            if searched in numbers_dictionary:
                del numbers_dictionary[searched]
            else:
                print('Number does not exist in dictionary')
                break
            line = input()

print(numbers_dictionary)