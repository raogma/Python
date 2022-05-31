def auto_init(klass, *args):
    attributes = klass.__annotations__
    for attr, value in zip(attributes, args):
        setattr(klass, attr, value)


class Person:
    __name: str
    __age: int
    __init__ = auto_init

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())