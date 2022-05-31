from abc import ABC, abstractmethod
from project.food import Food

data = {
    'Owl': {'sound': "Hoot Hoot", 'food': 'Meat', 'gain': 0.25},
    'Hen': {'sound': "Cluck", 'food': ('Vegetable', 'Fruit', 'Meat', 'Seed'), 'gain': 0.35},
    'Mouse': {'sound': "Squeak", 'food': ('Vegetable', 'Fruit'), 'gain': 0.1},
    'Dog': {'sound': "Woof!", 'food': 'Meat', 'gain': 0.4},
    'Cat': {'sound': "Meow", 'food': ('Vegetable', 'Meat'), 'gain': 0.3},
    'Tiger': {'sound': "ROAR!!!", 'food': 'Meat', 'gain': 1},
}


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        ...

    def feed(self, food: object):
        class_type = self.__class__.__name__
        food_name = food.__class__.__name__
        global data
        if food_name not in data[class_type]['food']:
            return f"{class_type} does not eat {food_name}!"
        self.food_eaten += food.quantity
        self.weight += data[class_type]['gain'] * food.quantity

    def __repr__(self):
        AnimalType = self.__class__.__name__
        AnimalName = self.name
        AnimalWeight = self.weight
        FoodEaten = self.food_eaten
        if AnimalType in ('Owl', 'Hen'):
            WingSize = self.wing_size
            return f"{AnimalType} [{AnimalName}, {WingSize}, {AnimalWeight}, {FoodEaten}]"
        AnimalLivingRegion = self.living_region
        return f"{AnimalType} [{AnimalName}, {AnimalWeight}, {AnimalLivingRegion}, {FoodEaten}]"


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def make_sound(self):
        global data
        return data[self.__class__.__name__]['sound']


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def make_sound(self):
        global data
        return data[self.__class__.__name__]['sound']
