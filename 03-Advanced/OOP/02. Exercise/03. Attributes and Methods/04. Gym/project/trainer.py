from typing import ClassVar


def auto_init(klass, *args):
    attributes = klass.__annotations__
    attributes = [x for x in attributes if x != 'id']

    for attr, value in zip(attributes, args):
        setattr(klass, attr, value)

    klass.id = klass.__class__.id
    klass.__class__.id += 1


class Trainer:
    name: str
    id: ClassVar[int] = 1

    __init__ = auto_init

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.id
