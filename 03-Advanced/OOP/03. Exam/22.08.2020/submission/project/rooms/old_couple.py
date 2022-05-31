from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(name=family_name, budget=pension_one + pension_two, members_count=2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove(), TV(), Fridge(), Stove()]

    def calculate_expenses(self, *args):
        super().calculate_expenses(self.appliances)
