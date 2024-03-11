# Create your models here.
from django.db import models


# Create your models here.

class Artiles(models.Model):
    title = models.CharField('Ім`я:', max_length=50)
    num = models.CharField('Номер телефону:', max_length=13)
    address = models.CharField('Адреса:', max_length=55)
    date = models.DateField('Дата народження:')
    info = models.CharField('Додаткова інформація:',max_length=700)

    def __str__(self):
        return f' Name: {self.title}'

    class Meta:
        verbose_name= 'Patient'
        verbose_name_plural = 'Patients'
