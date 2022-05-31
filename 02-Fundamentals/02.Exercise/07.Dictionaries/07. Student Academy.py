def append_to_dict(key, value, dictionary):
    if key not in dictionary.keys():
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)


def get_average(list):
    return sum(list) / len(list)


rows = int(input())

students = {}
filtered_students = {}

for _ in range(rows):
    student = input()
    grade = float(input())
    append_to_dict(student, grade, students)

for student, grades in students.items():
    if get_average(grades) >= 4.50:
        filtered_students[student] = get_average(grades)

[print(f'{student} -> {grade:.2f}') for student, grade in dict(sorted(filtered_students.items(), key=lambda el:el[1], reverse=True)).items()]