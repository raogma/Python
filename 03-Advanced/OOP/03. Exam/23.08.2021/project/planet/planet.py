class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

    def add_items(self, str_items):
        for item in str_items.split(', '):
            self.items.append(item)
