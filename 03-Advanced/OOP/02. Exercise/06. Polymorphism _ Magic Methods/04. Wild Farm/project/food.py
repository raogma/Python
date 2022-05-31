from abc import ABC


class Food(ABC):
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food, ABC):
    ...


class Fruit(Food, ABC):
    ...


class Meat(Food, ABC):
    ...


class Seed(Food, ABC):
    ...