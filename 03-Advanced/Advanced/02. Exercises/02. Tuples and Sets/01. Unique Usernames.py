input_count = int(input())
usernames = [input() for _ in range(input_count)]
[print(user) for user in set(usernames)]