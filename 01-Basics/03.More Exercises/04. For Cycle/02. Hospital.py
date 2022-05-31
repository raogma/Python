days = int(input())

doctors = 7
patients_untreated = 0
patients_treated = 0
total_patients_untreated = 0
total_patients_treated = 0

for days in range(1, days + 1):
    patients_per_day = int(input())
    if days % 3 == 0:
        if total_patients_untreated > total_patients_treated:
            doctors += 1
    if patients_per_day <= doctors:
        patients_treated = patients_per_day
    elif patients_per_day > doctors:
        patients_treated = doctors
        patients_untreated = patients_per_day - patients_treated
        total_patients_untreated += patients_untreated

    total_patients_treated += patients_treated

print(f"Treated patients: {total_patients_treated}.")
print(f"Untreated patients: {total_patients_untreated}.")
