def append_to_dict_list(key, value, dictionary):
    if key not in dictionary:
        dictionary[key] = []
    if value not in dictionary[key]:
        dictionary[key].append(value)


companies = {}

while True:
    command = input()
    if command == 'End':
        break

    company, employee = command.split(' -> ')
    append_to_dict_list(company, employee, companies)

for company, employees in sorted(companies.items()):
    print(company)
    for employee in companies[company]:
        print(f'-- {employee}')
