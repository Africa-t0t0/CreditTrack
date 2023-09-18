from django.db import models


class TarjetaDebito(models.Model):
    nombre = models.CharField(max_length=50)
    compania = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    saldo = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.compania}'


class TarjetaCredito(models.Model):
    nombre = models.CharField(max_length=50)
    compania = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    monto_maximo = models.IntegerField()
    monto_utilizado = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.compania}'


