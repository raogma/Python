from django.db import models

from Expenses.validators import MaxSizeValidator, check_only_letters, MinLengthValidator, not_negative_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            check_only_letters,

        )
    )
    last_name = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            check_only_letters,
        )
    )
    budget = models.FloatField(
        default=0,
        validators=(
            not_negative_validator,
        )
    )
    profile_image = models.ImageField(
        upload_to='profile_pics',
        validators=(
            MaxSizeValidator(5),
        ),
        null=True,
        blank=True,
    )

    def format_budget(self):
        return f'{self.budget:.2f}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


class Expense(models.Model):
    title = models.CharField(
        max_length=30
    )
    expense_image = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.FloatField()

    @property
    def format_price(self):
        return f'{self.price:.2f}'

    def __str__(self):
        return f'{self.title} - {self.format_price}$'
