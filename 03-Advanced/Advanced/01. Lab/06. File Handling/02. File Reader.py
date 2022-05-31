file = open(r'C:\Users\raich\Desktop\SoftUni\Advanced\01. Lab\06. File Handling\Files\numbers.txt')
sum = 0

for line in file:
    sum += int(line)

print(sum)
file.close()