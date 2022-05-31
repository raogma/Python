class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            room.calculate_expenses()
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        res = []
        i = 0
        while i <= len(self.rooms) - 1:
            room = self.rooms[i]
            if room.budget >= room.expenses + room.room_cost:
                res.append(f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {room.budget:.2f}$ left.")
                room.budget -= room.expenses + room.room_cost
                i += 1
            else:
                res.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return '\n'.join(res)

    def status(self):
        res = [f'Total population: {sum([x.members_count for x in self.rooms])}']
        for room in self.rooms:
            res.append(f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$')

            for child in room.children:
                res.append(f"--- Child {room.children.index(child) + 1} monthly cost: {child.cost * 30:.2f}$")

            res.append(f"--- Appliances monthly cost: {sum([x.get_monthly_expense() for x in room.appliances]):.2f}$")
        return '\n'.join(res)