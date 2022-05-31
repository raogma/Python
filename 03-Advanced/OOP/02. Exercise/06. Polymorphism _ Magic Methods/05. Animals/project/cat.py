from project.animal import Animal
from abc import ABC


class Cat(Animal, ABC):
    def make_sound(self):
        return 'Meow meow!'

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
