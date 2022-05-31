movie_name = input()
tickets = 0
student = 0
standard = 0
kid = 0

while movie_name != "Finish":
    total_tickets = int(input())
    ticket_type = input()
    while ticket_type != "End":
        tickets += 1
        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kid += 1
        if tickets >= total_tickets:
            break
        ticket_type = input()
    print(f"{movie_name} - {tickets * 100 / total_tickets:.2f}% full.")
    tickets = 0
    movie_name = input()

sum_tickets = student + kid + standard
print(f"Total tickets: {sum_tickets}")
print(f"{student * 100 / sum_tickets:.2f}% student tickets.")
print(f"{standard * 100 / sum_tickets:.2f}% standard tickets.")
print(f"{kid * 100 / sum_tickets:.2f}% kids tickets.")