from os import remove, path

if not path.exists(r'C:\Users\raich\Desktop\SoftUni\Advanced\01. Lab\06. File Handling\Files\my_first_file.txt'):
    print('File already deleted!')
else:
    remove(r'C:\Users\raich\Desktop\SoftUni\Advanced\01. Lab\06. File Handling\Files\my_first_file.txt')
