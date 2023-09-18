# Formulario django

from django import forms

from .models import Tarjeta

class AgregarTarjetaForm(forms.ModelForm):

    class Meta:
        model = Tarjeta
        fields = ['nombre', 'tipo_tarjeta', 'compania', 'banco', 'fecha_vencimiento', 'saldo', 'monto_maximo', 'monto_uitilizado', 'fecha_pago']

