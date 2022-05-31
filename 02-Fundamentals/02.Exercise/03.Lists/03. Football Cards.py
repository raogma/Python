cards = input().split()

team_A = [1] * 11
team_B = [1] * 11
isTerminated = False



for card in cards:
    element = card.split("-")
    team = element[0]
    player = int(element[1])
    if team == 'A':
        team_A[player - 1] = 0
    elif team == 'B':
        team_B[player - 1] = 0
    if sum(team_A) < 7 or sum(team_B) < 7:
        isTerminated = True
        break

print(f"Team A - {sum(team_A)}; Team B - {sum(team_B)}")
if isTerminated:
    print("Game was terminated")