from os import remove
folder_path = r'/home/rei/Desktop/SoftUni/Advanced/02. Exercises/06. File Handling/Files/03. FIle Manipulator Files'

while True:
    command = input()
    if command == 'End':
        break
    command = command.split('-')
    action, file_name = command[0], command[1]

    if action == 'Create':
        file = open(folder_path + '\\' + file_name, 'w')
        file.close()

    elif action == 'Add':
        content = command[2]
        with open(folder_path + '\\' + file_name, 'a') as file:
            file.write(f'{content}\n')

    elif action == 'Replace':
        old_string, new_string = command[2], command[3]
        try:
            with open(folder_path + '\\' + file_name, 'r') as file:
                text = file.read()
            with open(folder_path + '\\' + file_name, 'w') as file:
                file.write(text.replace(old_string, new_string))
        except FileNotFoundError:
            print('An error occurred')

    elif action == 'Delete':
        try:
            remove(folder_path + '\\' + file_name)
        except FileNotFoundError:
            print('An error occurred')
