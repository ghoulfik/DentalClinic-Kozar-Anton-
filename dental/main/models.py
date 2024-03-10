# Create your models here.
from django.db import models


# Create your models here.

class Artiles(models.Model):
    title = models.CharField('Name', max_length=50)
    num = models.CharField('Nums', max_length=13)
    address = models.CharField('Address', max_length=55)
    date = models.DateField()
    info = models.CharField(max_length=700)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Patient'
        verbose_name_plural = 'Patients'
