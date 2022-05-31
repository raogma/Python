from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        super().__init__(name=family_name, budget=salary, members_count=1)
        self.room_cost = 10
        self.appliances = [TV()]

    def calculate_expenses(self, *args):
        super().calculate_expenses(self.appliances)
