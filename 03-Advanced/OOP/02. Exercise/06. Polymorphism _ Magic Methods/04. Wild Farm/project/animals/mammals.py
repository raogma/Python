from abc import ABC
from project.animals.animal import Mammal


class Mouse(Mammal, ABC):
    ...


class Dog(Mammal, ABC):
    ...


class Cat(Mammal, ABC):
    ...


class Tiger(Mammal, ABC):
    ...