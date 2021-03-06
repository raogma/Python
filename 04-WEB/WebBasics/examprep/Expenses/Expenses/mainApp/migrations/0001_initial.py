# Generated by Django 4.0.2 on 2022-02-26 08:04

import Expenses.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2)])),
                ('budget', models.FloatField(default=0, validators=[django.core.validators.MinLengthValidator(0)])),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_pics', validators=[Expenses.validators.MaxSizeValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('expense_image', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
            ],
        ),
    ]
