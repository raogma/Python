class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.guests = []

    def add_guests(self, person):
        self.guests.append(person)

    def get_summary(self):
        all_guests = ', '.join([guest.name for guest in self.guests])
        return f"Going: {all_guests}\nTotal: {len(self.guests)}"


party = Party()

while True:
    command = input()
    if command == 'End':
        break

    persons_name = command
    person = Person(persons_name)
    party.add_guests(person)

print(party.get_summary())


