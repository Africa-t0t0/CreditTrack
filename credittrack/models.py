from django.db import models
from django.contrib.auth.models import User

TIPO_TARJETA = (
    ('credito', 'Credito'),
    ('debito', 'Debito'),
)

BANCOS = (
    ('bci', 'BCI'),
    ('bchile', 'Banco de Chile'),
    ('std', 'Santander'),
)

COMPANIA = (
    ('visa', 'Visa'),
    ('mastercard', 'Mastercard'),
)

class Tarjeta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=50)
    # credito o debito
    tipo_tarjeta = models.CharField(max_length=50, choices=TIPO_TARJETA)
    # mastercard, visa, etc
    compania = models.CharField(max_length=50, choices=COMPANIA)
    banco = models.CharField(max_length=50, choices=BANCOS)
    fecha_vencimiento = models.DateField()
    saldo = models.IntegerField(null=True, blank=True)
    monto_maximo = models.IntegerField(null=True, blank=True)
    monto_uitilizado = models.IntegerField(null=True, blank=True)
    fecha_pago = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.compania}'


