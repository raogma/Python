from django.db import models

from Project.validators import MinValueValidator, MaxValueValidator


class Game(models.Model):
    choices = 'Action, Adventure, Puzzle, Strategy, Sports, Board/Card Game, Other'.split(', ')

    title = models.CharField(
        max_length=30,
        unique=True,
    )
    category = models.CharField(
        max_length=max([len(x) for x in choices]),
        choices=[(x, x) for x in choices],
    )
    rating = models.FloatField(
        validators=(
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        )
    )
    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(1),
        )
    )
    image_URL = models.URLField()
    summary = models.TextField(
        null=True,
        blank=True,
    )
