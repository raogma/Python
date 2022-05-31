def append_to_dict(key, value, dictionary):
    if key not in dictionary.keys():
         dictionary[key] = value
         return f"{key} registered {value} successfully"
    else:
        return f"ERROR: already registered with plate number {dictionary[key]}"


def remove_from_dict(key, dictionary):
    if key not in dictionary:
        return f"ERROR: user {key} not found"
    else:
        del dictionary[key]
        return f"{key} unregistered successfully"


n = int(input())
parking = {}

for _ in range(n):
    command = input().split(maxsplit=1)
    if command[0] == 'register':
        username, plate = command[1].split(maxsplit=1)
        print(append_to_dict(username, plate, parking))
    else:
        username = command[1]
        print(remove_from_dict(username, parking))

[print(f"{key} => {value}")for key, value in parking.items()]