from re import finditer

username_pattern = r'(U\$)[A-Z][a-z][a-z]+\1'
password_pattern = r'(P@\$)[A-Za-z]{5,}\d+\1'
count = 0

for _ in range(int(input())):
    registration = input()
    password, username = str(), str()
    for element in finditer(username_pattern, registration):
        username = element.group()
        username = username.strip('U$')
    for element in finditer(password_pattern, registration):
        password = element.group()
        password = password.strip('P@$')

    if len(password) > 1 and len(username) > 1:
        print(f'Registration was successful')
        print(f'Username: {username}, Password: {password}')
        count += 1
    else:
        print('Invalid username or password')

print(f'Successful registrations: {count}')
