# Formulario django

from django import forms
from django_select2.forms import ModelSelect2Widget

from .models import Tarjeta, Transaccion

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

class AgregarTarjetaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, required=True, label='Nombre')
    tipo_tarjeta = forms.ChoiceField(
        choices=TIPO_TARJETA,
        required=True,
        label='Tipo de Tarjeta',
        widget=forms.Select(attrs={'style': 'text-transform: capitalize;'})
    )

    compania = forms.ChoiceField(
        choices=COMPANIA,
        required=True,
        label='Compañia',
        widget=forms.Select(attrs={'style': 'text-transform: capitalize;'})
    )

    banco = forms.ChoiceField(
        choices=BANCOS,
        required=True,
        label='Banco',
        widget=forms.Select(attrs={'style': 'text-transform: capitalize;'})
    )


    class Meta:
        model = Tarjeta
        fields = ['nombre', 'tipo_tarjeta', 'compania', 'banco', 'fecha_vencimiento', 'saldo', 'monto_maximo', 'fecha_pago']


class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        exclude=['activa']

