num_of_tabs = int(input())
salary = float(input())

fine = 0

for num_of_tabs in range(1, num_of_tabs + 1):
    tab = input()
    if tab == "Facebook":
        fine += 150
    elif tab == "Instagram":
        fine += 100
    elif tab == "Reddit":
        fine += 50
    if salary - fine <= 0:
        print("You have lost your salary.")
        break
if salary - fine > 0:
    print(f"{int(salary - fine)}")

