from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=64, verbose_name='Name')
    code = models.CharField(max_length=32, verbose_name='Code')
    price = models.FloatField( verbose_name='Price')
    date =  models.DateTimeField(verbose_name='Date')

    def __str__(self):
        return self.name