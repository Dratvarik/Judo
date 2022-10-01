# Generated by Django 4.0.5 on 2022-09-30 21:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season_tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_ticket', models.IntegerField(verbose_name='Абонемент')),
            ],
            options={
                'verbose_name': 'абонемент',
                'verbose_name_plural': 'Абонементы',
            },
        ),
        migrations.CreateModel(
            name='Treners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('middlename', models.CharField(max_length=50, verbose_name='Отчество')),
                ('FIO_coach', models.CharField(db_index=True, max_length=100, verbose_name='ФИО тренера')),
            ],
            options={
                'verbose_name': 'тренер',
                'verbose_name_plural': 'Тренеры',
            },
        ),
        migrations.CreateModel(
            name='Userss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
            ],
            options={
                'verbose_name': 'желающий',
                'verbose_name_plural': 'Желающие',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_section', models.CharField(max_length=50, verbose_name='Название секции')),
                ('idgroup', models.IntegerField(db_index=True, verbose_name='Номер группы')),
                ('quantity_in_week', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)], verbose_name='Кол-во занятий/неделя')),
                ('cost', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)], verbose_name='Стоимость')),
                ('FIO_coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='useris.treners', verbose_name='ФИО тренера')),
            ],
            options={
                'verbose_name': 'группа',
                'verbose_name_plural': 'Группы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('middlename', models.CharField(max_length=50, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Дата рождения')),
                ('payment', models.BooleanField(default=False, verbose_name='Оплата')),
                ('date_of_pay', models.DateField(null=True, verbose_name='Дата посл. оплаты')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('name_section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='useris.groups', verbose_name='Группа')),
                ('season_ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='useris.season_tickets', verbose_name='Абонемент')),
            ],
            options={
                'verbose_name': 'ребёнок',
                'verbose_name_plural': 'Дети',
            },
        ),
    ]
