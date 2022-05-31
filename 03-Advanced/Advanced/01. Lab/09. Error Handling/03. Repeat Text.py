msg = input()
count = input()
try:
    count = int(count)
    print(msg * count)
except ValueError:
    print('Variable count must be an integer')

