from django.db import models

from MusicApp.validators import MinLengthValidator, username_validator, not_negative_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            username_validator,
        )
    )
    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            not_negative_validator,
        )
    )

    def __str__(self):
        return f'{self.username}'


class Album(models.Model):
    genresList = [
         ("Pop Music", "Pop Music"),
         ("Jazz Music", "Jazz Music"),
         ("R&B Music", "R&B Music"),
         ("Rock Music", "Rock Music"),
         ("Country Music", "Country Music"),
         ("Dance Music", "Dance Music"),
         ("Hip Hop Music", "Hip Hop Music"),
         ("Other", "Other"),
    ]

    album_name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Album Name'
    )
    artist = models.CharField(
        max_length=30,
    )
    genre = models.CharField(
        max_length=30,
        choices=genresList,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_URL = models.URLField()

    price = models.FloatField(
        validators=(
            not_negative_validator,
        )
    )

    @property
    def format_price(self):
        return f'${self.price:.2f}'

    def __str__(self):
        return self.album_name
