from abc import ABC


class Drink(ABC):
    def __init__(self, name: str, portion: int, price: float, brand: str):
        self.__name = name
        self.__portion = portion
        self.__price = price
        self.__brand = brand

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value == '' or value == ' ':
            raise ValueError("Brand cannot be empty string or white space!")

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"