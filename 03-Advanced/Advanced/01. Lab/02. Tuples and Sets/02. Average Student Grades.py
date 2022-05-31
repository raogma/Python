input_count = int(input())

statistics = dict()

for _ in range(input_count):
    name, grade = input().split()
    if name not in statistics:
        statistics[name] = [float(grade), ]
    else:
        statistics[name].append(float(grade))
############################### notes
[print(f'{name} -> {" ".join(f"{grade:.2f}" for grade in grades)} '
       f'(avg: {sum(grades) / len(grades):.2f})') for name, grades in statistics.items()]