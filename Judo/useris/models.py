from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Children (models. Model):
    surname=models.CharField(max_length=50, verbose_name= 'Фамилия')
    name=models.CharField(max_length=50, verbose_name='Имя')
    middlename=models.CharField(max_length=50, verbose_name='Отчество')
    idgroup=models.IntegerField(verbose_name='Группа')
    age=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)], verbose_name='Возраст')
    height=models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(150)], verbose_name='Рост', blank=True)
    weight=models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(230)], verbose_name='Вес', blank=True)
    payment=models.BooleanField(default=False, verbose_name='Оплата')

