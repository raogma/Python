phonebook = dict()

while True:
    line = input()
    if line.isdigit():
        break
    else:
        person, number = line.split('-')
        phonebook[person] = number

for _ in range(int(line)):
    searched_person = input()
    if searched_person in phonebook:
        print(f'{searched_person} -> {phonebook[searched_person]}')
    else:
        print(f'Contact {searched_person} does not exist.')