from django.db import models
from django.contrib.auth.models import User

TIPO_TARJETA = (
    ('credito', 'Credito'),
    ('debito', 'Debito'),
)

BANCOS = (
    ('bci', 'BCI'),
    ('bch', 'Banco de Chile'),
    ('std', 'Santander'),
)

COMPANIA = (
    ('Visa', 'visa'),
    ('Mastercard', 'mastercard'),
)

class Tarjeta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=50)
    # credito o debito
    tipo_tarjeta = models.CharField(max_length=50)
    # mastercard, visa, etc
    compania = models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    saldo = models.IntegerField(null=True, blank=True)
    monto_maximo = models.IntegerField(null=True, blank=True)
    monto_utilizado = models.IntegerField(null=True, blank=True)
    fecha_pago = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.compania}'


class Transaccion(models.Model):
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    monto = models.IntegerField('Monto')
    cuota_actual = models.IntegerField('Cuota actual', null=True, blank=True)
    n_cuotas = models.IntegerField('Numero de cuotas')
    fecha = models.DateField('Fecha de transaccion')
    descripcion = models.CharField('Descripcion', max_length=100)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.tarjeta} - {self.monto} - {self.fecha}'
