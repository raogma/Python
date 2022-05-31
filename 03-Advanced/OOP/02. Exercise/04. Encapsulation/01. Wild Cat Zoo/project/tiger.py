from project.animal import Animal


class Tiger(Animal):
    get_needs = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.__class__.get_needs)
