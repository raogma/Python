allowed_fails = int(input())
name_of_exercise = input()

fails = 0
rating_sum = 0
exercises_counter = 0
last_exercise = ""

while name_of_exercise != "Enough":
    last_exercise = name_of_exercise
    rating = int(input())
    exercises_counter += 1
    if rating <= 4:
        fails += 1
        if fails == allowed_fails:
            print(f"You need a break, {fails} poor grades.")
            break
    rating_sum += rating
    name_of_exercise = input()
else:
    print(f"Average score: {rating_sum / exercises_counter:.2f}")
    print(f"Number of problems: {exercises_counter}")
    print(f"Last problem: {last_exercise}")