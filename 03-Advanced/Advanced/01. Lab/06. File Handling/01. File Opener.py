try:
    open(r'C:\Users\raich\Desktop\SoftUni\Advanced\01. Lab\06. File Handling\Files\xt.txt')
    print('File found')
except FileNotFoundError:
    print('File not found')
