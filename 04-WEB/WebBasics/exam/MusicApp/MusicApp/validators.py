import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MinLengthValidator:
    def __init__(self, length):
        self.length = length

    def __call__(self, value):
        if len(value) < self.length:
            raise ValidationError('Value must be at least 2 characters long!')


def username_validator(value):
    matchArr = re.findall('\w+', value)
    if len(matchArr) > 1:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def not_negative_validator(value):
    if value < 0:
        raise ValidationError('Value must be positive!')

