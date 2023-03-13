from .models import OrderCharger
from django.forms import ModelForm, TextInput, Textarea


class OrderChargerFrom(ModelForm):
    class Meta:
        model = OrderCharger
        fields = ["id_charge","title", "task","slot_number","car_title","battery_voltage","start_charge_time","status","charge_percent","end_charge_time"]
        widgets = {
            "id_charge": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Заправка №"

            }),
            "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введите название"

            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание"

            }),
            "slot_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Номер парковки"

            }),
            "car_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Марка автомобиля"

            }),
            "battery_voltage": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Напряжение батареи"

            }),
            "start_charge_time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Время начало заправки"

            }),
            "status": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Статус парковки"

            }),
            "charge_percent": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Процент зарядки"

            }),
            "end_charge_time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Время окончания заряда"

            }),
        }

