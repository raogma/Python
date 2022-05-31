income = float(input())
grade = float(input())
min_salary = float(input())

soc_scholarship = 0.35 * min_salary


exc_scholarship = 25 * grade

if grade <= 4.5:
    print("You cannot get a scholarship!")

elif 4.5 < grade < 5.5:
    if income < min_salary:
        print(f"You get a Social scholarship {int(soc_scholarship)} BGN")
    else:
        print("You cannot get a scholarship!")

elif grade >= 5.5:
    if income >= min_salary:
        print(f"You get a scholarship for excellent results {int(exc_scholarship)} BGN")
    else:
        if soc_scholarship > exc_scholarship:
            print(f"You get a Social scholarship {int(soc_scholarship)} BGN")
        else:
            print(f"You get a scholarship for excellent results {int(exc_scholarship)} BGN")
