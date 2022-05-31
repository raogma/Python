class Room:
    def __init__(self, name: str, budget: float, members_count:int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.__children = []
        self.__expenses = 0

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        self.__children = value

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total = 0
        for el in args:
            for x in el:    # or .cost?
                total += x.cost
        self.__expenses = total
