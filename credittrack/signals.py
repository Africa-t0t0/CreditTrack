from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transaccion, Tarjeta

@receiver(post_save, sender=Transaccion)
def actualizar_monto_tarjeta(sender, instance, **kwargs):
    tarjeta = instance.tarjeta
    if tarjeta.tipo_tarjeta == 'debito' or tarjeta.tipo_tarjeta == 'Debito':
        tarjeta.saldo -= instance.monto
        tarjeta.save()
    else:
        tarjeta.monto_utilizado += instance.monto
        tarjeta.save()

@receiver(post_delete, sender=Transaccion)
def restar_monto_tarjeta(sender, instance, **kwargs):
    tarjeta = instance.tarjeta
    if tarjeta.tipo_tarjeta == 'debito' or tarjeta.tipo_tarjeta == 'Debito':
        tarjeta.saldo += instance.monto
        tarjeta.save()
    else:
        tarjeta.monto_utilizado -= instance.monto
        tarjeta.save()