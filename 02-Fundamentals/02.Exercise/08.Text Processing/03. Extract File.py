path = input()

for i in range(len(path)):
    if path[i] == '\ '.rstrip():
        saved_index = i

path = path.replace(path[0:saved_index + 1], str())
path = path.split('.')

print(f'''
File name: {path[0]}
File extension: {path[1]}
''')