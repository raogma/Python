class Topping:
    def __init__(self, topping_type, weight: float):
        self.__topping_type = topping_type
        if self.__topping_type == '':
            raise ValueError("The topping type cannot be an empty string")
        self.__weight = weight
        if self.__weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):
        self.topping_type = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value