from typing import ClassVar


def auto_init(self, *args):
    attributes = self.__annotations__
    attributes = [x for x in attributes if x != 'id']

    for attr, value in zip(attributes, args):
        setattr(self, attr, value)

    self.id = self.__class__.id
    self.__class__.id += 1


class ExercisePlan:
    trainer_id: int
    equipment_id: int
    duration: int
    id: ClassVar[int] = 1

    __init__ = auto_init

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        return cls(trainer_id, equipment_id, hours * 60)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @staticmethod
    def get_next_id():
        return ExercisePlan.id