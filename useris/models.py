from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Season_tickets(models. Model):
    season_ticket=models.IntegerField(verbose_name='Абонемент')
    # validators=[MinValueValidator(1), MaxValueValidator(13),], 
    def __str__(self):
        return str(self.season_ticket)

    class Meta:
        verbose_name='абонемент'
        verbose_name_plural='Абонементы'

class Treners(models.Model):
    surname=models.CharField(max_length=50, verbose_name= 'Фамилия')
    name=models.CharField(max_length=50, verbose_name='Имя')
    middlename=models.CharField(max_length=50, verbose_name='Отчество')
    FIO_coach=models.CharField(max_length=100, db_index=True, verbose_name= 'ФИО тренера')


    def __str__(self):
        return self.FIO_coach

    class Meta:
        verbose_name='тренер'
        verbose_name_plural='Тренеры'

class Groups(models.Model):
    name_section=models.CharField(max_length=50, verbose_name= 'Название секции')
    idgroup=models.IntegerField(verbose_name='Номер группы', db_index=True)
    quantity_in_week=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)], verbose_name='Кол-во занятий/неделя')
    cost=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)], verbose_name='Стоимость')
    FIO_coach=models.ForeignKey(Treners, on_delete=models.PROTECT, null=True, verbose_name='ФИО тренера')

    def __str__(self):
        return self.name_section

    class Meta:
        verbose_name='группа'
        verbose_name_plural='Группы'
        ordering=['id']

class Children (models. Model):
    surname=models.CharField(max_length=50, verbose_name= 'Фамилия')
    name=models.CharField(max_length=50, verbose_name='Имя')
    middlename=models.CharField(max_length=50, verbose_name='Отчество')
    idgroup=models.ManyToManyField (Groups, db_table='sostav_groups', verbose_name='Группа')
    date_of_birth=models.DateField( null=True, verbose_name='Дата рождения')
    payment=models.BooleanField(default=False, verbose_name='Оплата')
    date_of_pay=models.DateField(null=True, verbose_name='Дата посл. оплаты')
    season_ticket=models.ForeignKey(Season_tickets, on_delete=models.PROTECT, null=True, verbose_name='Абонемент')
    comments=models.TextField(verbose_name='Комментарии', null=True, blank=True)

    # def get_idgroup(self):
    #     return "\n".join([p.groups for p in self.idgroup.all()])

    def __str__(self):
        return self.surname
        # , self.name, self.middlename

    class Meta:
        verbose_name='ребёнок'
        verbose_name_plural='Дети'
        # ordering=['-created_at', 'title']

class Userss(models.Model):
    name=models.CharField(max_length=150, verbose_name='Имя')
    phone=models.CharField(max_length=200, verbose_name='Телефон')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name='желающий'
        verbose_name_plural='Желающие'