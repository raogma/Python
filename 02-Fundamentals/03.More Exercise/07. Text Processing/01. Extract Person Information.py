from re import finditer

regex = r'(?P<name>@[A-Za-z]+\|)|(?P<age>#\d{1,2}\*)'

for _ in range(int(input())):
    data = {'name': str(), 'age': int()}
    for element in finditer(regex, input()):
        element = element.group()
        element = element[1: len(element) - 1]
        if element.isalpha():
            data['name'] = element
        else:
            data['age'] = element
    print(f'{data["name"]} is {data["age"]} years old.')