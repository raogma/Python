movie_name = input()
student = 0
standard = 0
kid = 0
seats_counter = 0
total_seats = 0

while movie_name != "Finish":
    total_seats = int(input())
    ticket_type = input()
    while ticket_type != "End":
        seats_counter += 1
        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kid += 1
        if total_seats <= 0:
            break
        ticket_type = input()
        if seats_counter >= total_seats:
            break
    if seats_counter >= total_seats:
        break
    print(f"{movie_name} - {seats_counter * 100 / total_seats:.2f}% full.")
    movie_name = input()
else:
    print(f"Total tickets: {seats_counter}")
    print(f"{student * 100 / seats_counter:.2f}% student tickets.")
    print(f"{standard * 100 / seats_counter:.2f}% standard tickets.")
    print(f"{kid * 100 / seats_counter:.2f}% kid tickets.")