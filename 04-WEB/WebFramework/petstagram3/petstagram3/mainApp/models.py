from datetime import date

from django.contrib.auth import get_user_model
from django.db import models

from petstagram3.mainApp.validators import validate_5mb_size, validate_min_len, validate_only_letters

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        validators=(
            validate_min_len,
            validate_only_letters
        )
    )
    last_name = models.CharField(
        max_length=30,
        validators=(
            validate_min_len,
            validate_only_letters
        )
    )

    avatar = models.URLField(
        null=True,
        blank=True,  # should remove in the end
    )

    birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    genders_list = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Do not show", "Do not show")
    ]
    gender = models.CharField(
        max_length=max([len(x) for x, _ in genders_list]),
        choices=genders_list,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )

    types_list = [
        ("Cat", "Cat"),
        ("Dog", "Dog"),
        ("Bunny", "Bunny"),
        ("Parrot", "Parrot"),
        ("Fish", "Fish"),
        ("Other", "Other")
    ]
    type = models.CharField(
        max_length=max([len(x) for x, _ in types_list]),
        choices=types_list
    )

    birth = models.DateField(
        verbose_name='Date of Birth'
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))

    def __str__(self):
        return f'{self.name} ({self.type})'

    class Meta:
        unique_together = ('name', 'owner')


class PetPhoto(models.Model):
    photo = models.ImageField(
        upload_to='pet_photos/',
        validators=(
            validate_5mb_size,
        )
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
