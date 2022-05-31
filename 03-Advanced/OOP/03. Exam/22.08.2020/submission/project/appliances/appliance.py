class Appliance:
    def __init__(self, cost: float):
        self.__cost = cost

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        self.__cost = value

    def get_monthly_expense(self):
        return self.cost * 30
