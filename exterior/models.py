from django.contrib.auth.models import User
from django.db import models

from simple_history.models import HistoricalRecords



class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField()
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.IntegerField(default=0)
    total = models.FloatField()
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.total = self.producto.precio * self.cantidad
        super(Compra, self).save(*args, **kwargs)

    def __str__(self):
        return self.orden.cliente.username + " " + self.producto.nombre


class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre