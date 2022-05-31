from datetime import datetime

from django.core.exceptions import ValidationError


def validate_min_len(value):
    if len(value) < 2:
        raise ValidationError('Name must be at least 2 letters long!')


def validate_only_letters(value):
    for x in value:
        if not x.isalpha():
            raise ValidationError('Name should consists only of letters!')


def validate_5mb_size(value):
    if value.file.size > 5 * 1024 * 1024:
        raise ValidationError('File size should be less than 5MB!')
