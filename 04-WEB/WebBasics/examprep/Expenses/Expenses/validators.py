from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def check_only_letters(value):
    for x in value:
        if not x.isalpha():
            raise ValidationError("Ensure this value contains only letters.")


@deconstructible
class MaxSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.convert_into_mb(self.max_size):
            raise ValidationError(f"Max file size is {filesize:.2f} MB")

    @staticmethod
    def convert_into_mb(value):
        return value * 1024 * 1024


@deconstructible
class MinLengthValidator:
    def __init__(self, length):
        self.length = length

    def __call__(self, value):
        if len(value) < self.length:
            raise ValidationError('Value must be at least 2 characters long!')


def not_negative_validator(value):
    if value < 0:
        raise ValidationError('Value must be positive!')
