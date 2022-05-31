class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    command = input()
    if command == 'End':
        break
    persons_name = command
    party.people.append(persons_name)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")