# Generated by Django 4.1.7 on 2023-03-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercharger',
            name='battery_voltage',
            field=models.CharField(default='0', max_length=50, verbose_name='Напряжение батареи'),
        ),
        migrations.AddField(
            model_name='ordercharger',
            name='car_title',
            field=models.CharField(default='Не указано', max_length=50, verbose_name='Название автомобиля'),
        ),
        migrations.AddField(
            model_name='ordercharger',
            name='slot_number',
            field=models.IntegerField(default=0, verbose_name='Номер стоянки'),
        ),
        migrations.AddField(
            model_name='ordercharger',
            name='start_charge_time',
            field=models.CharField(default='Не указано', max_length=50, verbose_name='Время начало заправки'),
        ),
        migrations.AddField(
            model_name='ordercharger',
            name='status',
            field=models.IntegerField(default=4, verbose_name='Статус стоянки №'),
        ),
    ]
