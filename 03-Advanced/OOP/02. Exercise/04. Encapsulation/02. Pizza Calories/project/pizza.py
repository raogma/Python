class Pizza:
    def __init__(self,
                 name: str,
                 dough: object,
                 toppings_capacity: int):
        self.__name = name
        if self.__name == '':
            raise ValueError("The name cannot be an empty string")
        self.__dough = dough
        if self.__dough is None:
            raise ValueError("You should add dough to the pizza")
        self.__toppings_capacity = toppings_capacity
        if self.__toppings_capacity <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings = {}
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def dough(self):
        return self.__dough
    
    @dough.setter
    def dough(self, value):
        self.__dough = value
        
    @property
    def toppings_capacity(self):
        return self.__toppings_capacity
    
    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value
        
    @property
    def toppings(self):
        return self.__toppings
    
    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    def add_topping(self, topping: object):
        if self.__toppings_capacity <= 0:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.__toppings:
            self.__toppings[topping.topping_type] += topping.weight
        else:
            self.__toppings[topping.topping_type] = topping.weight
        self.__toppings_capacity -= 1

    def calculate_total_weight(self):
        toppings_total = sum([x for x in self.__toppings.values()])
        return toppings_total + self.__dough.weight
