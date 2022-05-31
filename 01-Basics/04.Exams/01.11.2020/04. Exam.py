students = int(input())

fail = 0
average = 0
good = 0
excellent = 0
grade_total = 0

for students in range(1, students + 1):
    grade = float(input())
    grade_total += grade
    if 2 <= grade <= 2.99:
        fail += 1
    elif 3 <= grade <= 3.99:
        average += 1
    elif 4 <= grade <= 4.99:
        good += 1
    elif grade >= 5:
        excellent += 1

# students * x/100 = fail
fail_perc = fail * 100 / students
average_perc = average * 100 / students
good_perc = good * 100 / students
excellent_perc = excellent * 100 / students
total_average_grade = grade_total / students

print(f"Top students: {excellent_perc:.2f}%")
print(f"Between 4.00 and 4.99: {good_perc:.2f}%")
print(f"Between 3.00 and 3.99: {average_perc:.2f}%")
print(f"Fail: {fail_perc:.2f}%")
print(f"Average: {total_average_grade:.2f}")
