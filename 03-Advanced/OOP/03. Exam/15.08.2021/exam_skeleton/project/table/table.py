from abc import ABC


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: object):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: object):
        self.drink_orders.append(drink)

    def get_bill(self):
        total = 0
        for element in self.food_orders:
            total += element.price
        for element in self.drink_orders:
            total += element.price
        return total

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f""""Table: {self.table_number}
Type: {self.__class__.__name__}
Capacity: {self.capacity}"""

