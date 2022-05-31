from abc import ABC, abstractmethod


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @property
    def oxygen(self):
        return self.__oxygen

    @oxygen.setter
    def oxygen(self, value):
        self.__oxygen = value

    @abstractmethod
    def breathe(self):
        self.__oxygen -= 10

    def increase_oxygen(self, amount):
        self.__oxygen += amount


