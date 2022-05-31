def append_to_dict_list(key, value, dictionary):
    if key not in dictionary.keys():
         dictionary[key] = [value]
    else:
        dictionary[key].append(value)


courses = {}

while True:
    command = input()
    if command == 'end':
        break
    course, student = command.split(' : ')
    append_to_dict_list(course, student, courses)
for program, list in dict(sorted(courses.items(), key=lambda el: len(el[1]), reverse=True)).items():
    print(f"{program}: {len(list)}")
    for element in sorted(list):
        print(f"-- {element}")