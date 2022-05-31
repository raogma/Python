from typing import ClassVar


def auto_init(klass, *args):
    attributes = klass.__annotations__
    attributes = [x for x in attributes if x != 'id']

    for attribute, value in zip(attributes, args):
        setattr(klass, attribute, value)

    klass.id = klass.__class__.id
    klass.__class__.id += 1


class Customer:
    name: str
    address: str
    email: str
    id: ClassVar[int] = 1

    __init__ = auto_init

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; \
Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.id
