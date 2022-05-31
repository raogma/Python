class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: object):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for r in self.rooms:
            total_consumption += r.expenses + r.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        res = ''
        i = 0
        while i < len(self.rooms):
            r = self.rooms[i]
            if r.expenses + r.room_cost <= r.budget:
                res += f"{r.family_name} paid {r.expenses+r.room_cost:.2f}$ and have {r.budget:.2f}$ left.\n"
                r.budget -= r.expenses + r.room_cost
                i += 1
            else:
                res += f"{r.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(r)
        return res[:-1]

    def status(self):
        people = sum([r.members_count for r in self.rooms])
        res = f'Total population: {people}\n'
        for r in self.rooms:
            res += f'{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$\n'
            for c in r.children:
                res += f'--- Child {r.children.index(c) + 1} monthly cost: {c.get_monthly_expense():.2f}$\n'
            res += f'--- Appliances monthly cost: {sum([a.get_monthly_expense() for a in r.appliances]):.2f}$\n'
        return res[:-1]
