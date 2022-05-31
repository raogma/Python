from project.appliances.appliance import Appliance


class Laptop(Appliance):
    cost = 1

    def __init__(self):
        super().__init__(cost=self.__class__.cost)
