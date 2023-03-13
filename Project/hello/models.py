from django.db import models
#CREATE DB HERE

class OrderCharger(models.Model):
    id_charge = models.IntegerField("Заправка №")
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    slot_number = models.IntegerField("Номер парковки",null=True)
    car_title = models.CharField('Марка автомобиля', max_length=50, null=True)
    battery_voltage = models.CharField('Напряжение батареи', max_length=50, null=True)
    start_charge_time = models.CharField('Время заправки', max_length=50, null=True)
    status =  models.IntegerField("Статус парковочного места",null=True)
    #1 - занята, 2 - свободна, 3 - на тех обслуживание 4 - закрыта
    charge_percent = models.FloatField("Текущий процент зарядки", null=True)
    end_charge_time = models.CharField('Время окончания заправки', max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Машины на зарядке'
        verbose_name_plural = "Все машины на зарядке"