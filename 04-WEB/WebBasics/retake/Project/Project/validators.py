from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MinValueValidator:
    def __init__(self, validator):
        self.validator = validator

    def __call__(self, value):
        if value < self.validator:
            raise ValidationError(f'The value cannot be below {self.validator}')


@deconstructible
class MaxValueValidator:
    def __init__(self, validator):
        self.validator = validator

    def __call__(self, value):
        if value > self.validator:
            raise ValidationError(f"The value can't be above {self.validator}")
