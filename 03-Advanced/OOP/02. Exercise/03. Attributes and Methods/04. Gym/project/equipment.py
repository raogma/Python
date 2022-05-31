from typing import ClassVar


def auto_init(self, *args):
    attributes = self.__annotations__
    attributes = [x for x in attributes if x != 'id']

    for attr, value in zip(attributes, args):
        setattr(self, attr, value)

    self.id = self.__class__.id
    self.__class__.id += 1


class Equipment:
    name: str
    id: ClassVar[int] = 1
    __init__ = auto_init

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.id
