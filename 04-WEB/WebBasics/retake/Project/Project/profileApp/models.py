from django.db import models

from Project.validators import MinValueValidator


class Profile(models.Model):
    email = models.EmailField()
    age = models.IntegerField(
        validators=(
            MinValueValidator(12),
        ),
    )
    password = models.CharField(
        max_length=30,
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return f'{self.first_name}'
        elif self.last_name:
            return f'{self.last_name}'


