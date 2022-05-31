judges = int(input())
sum_grades = 0
counter = 0
average = 0
sum_average = 0
name_of_presentation = input()
while name_of_presentation != "Finish":
    counter += 1
    for judges in range(1, judges + 1):
        grades = float(input())
        sum_grades += grades
    average = sum_grades / judges
    print(f"{name_of_presentation} - {average:.2f}.")
    sum_grades = 0
    sum_average += average
    average = 0
    name_of_presentation = input()

print(f"Student's final assessment is {sum_average / counter:.2f}.")