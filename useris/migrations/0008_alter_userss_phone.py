# Generated by Django 4.0.5 on 2022-08-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useris', '0007_alter_userss_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userss',
            name='phone',
            field=models.CharField(max_length=200, verbose_name='Телефон'),
        ),
    ]
