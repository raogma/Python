# Generated by Django 4.0.2 on 2022-02-26 10:21

import Expenses.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='budget',
            field=models.FloatField(default=0, validators=[Expenses.validators.not_negative_validator]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=15, validators=[Expenses.validators.MinLengthValidator(2), Expenses.validators.check_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=15, validators=[Expenses.validators.MinLengthValidator(2), Expenses.validators.check_only_letters]),
        ),
    ]