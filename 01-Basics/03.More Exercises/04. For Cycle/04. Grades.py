num_of_students = int(input())

top_students = 0
good_students = 0
average_students = 0
fail_students = 0
sum_of_grade = 0

for num_of_students in range(1, num_of_students + 1):
    grade = float(input())
    sum_of_grade += grade
    if grade <= 2.99:
        fail_students += 1
    elif grade <= 3.99:
        average_students += 1
    elif grade <= 4.99:
        good_students += 1
    else:
        top_students += 1

perc_fail_students = fail_students * 100 / num_of_students
perc_average_students = average_students * 100 / num_of_students
perc_good_students = good_students * 100 / num_of_students
perc_top_students = top_students * 100 / num_of_students
average_grade = sum_of_grade / num_of_students

print(f"Top students: {perc_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {perc_good_students:.2f}%")
print(f"Between 3.00 and 3.99: {perc_average_students:.2f}%")
print(f"Fail: {perc_fail_students:.2f}%")
print(f"Average: {average_grade:.2f}")