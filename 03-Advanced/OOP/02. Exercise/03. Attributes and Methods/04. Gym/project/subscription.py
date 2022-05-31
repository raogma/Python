from typing import ClassVar


def auto_init(self, *args):
    attributes = self.__annotations__
    attributes = [x for x in attributes if x != 'id']

    for attr, value  in zip(attributes, args):
        setattr(self, attr, value)

    self.id = self.__class__.id
    self.__class__.id += 1


class Subscription:
    date: str
    customer_id: int
    trainer_id: int
    exercise_id: int
    id: ClassVar[int] = 1

    __init__ = auto_init

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @staticmethod
    def get_next_id():
        return Subscription.id
