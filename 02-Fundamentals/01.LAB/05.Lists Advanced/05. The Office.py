string = input().split()
factor = int(input())
employees = [int(element) * factor for element in string]

average = sum(employees) / len(employees)
happy_count = 0

for element in employees:
    if element >= average:
        happy_count += 1

print(f"Score: {happy_count}/{len(employees)}. Employees are happy!") if happy_count >= len(employees) / 2 \
    else print(f"Score: {happy_count}/{len(employees)}. Employees are not happy!")