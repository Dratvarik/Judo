# Generated by Django 4.0.5 on 2022-07-20 10:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('middlename', models.CharField(max_length=50, verbose_name='Отчество')),
                ('idgroup', models.IntegerField(verbose_name='Группа')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)], verbose_name='Возраст')),
                ('height', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(150)], verbose_name='Рост')),
                ('weight', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(230)], verbose_name='Вес')),
                ('payment', models.BooleanField(default=False, verbose_name='Оплата')),
            ],
        ),
    ]