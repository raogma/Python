usernames = input().split(', ')

build_username = str()
for username in usernames:
    if 3 <= len(username) <= 16:
        isValid = True
        for symbol in username:
            if not (symbol.isalnum() or symbol == '-' or symbol == '_'):
                build_username += symbol
                isValid = False
        if isValid:
            print(username)