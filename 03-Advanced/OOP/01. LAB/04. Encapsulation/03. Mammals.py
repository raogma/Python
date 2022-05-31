def auto_init(klass, *args):
    attributes = klass.__annotations__
    for attr, value in zip(attributes, args):
        setattr(klass, attr, value)


class Mammal:
    name: str
    type: str
    sound: str
    __kingdom: str = 'animals'
    __init__ = auto_init

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())