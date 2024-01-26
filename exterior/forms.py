from django import forms


from .models import Compra, Estado, Proveedor, Producto

class CompraForm(forms.ModelForm):
    estado = forms.ModelChoiceField(
        queryset=Estado.objects.all(),
        required=True,
        label='Estado',
        widget=forms.Select(attrs={'style': 'text-transform: capitalize;'})
    )
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        required=True,
        label='Proveedor',
        widget=forms.Select(attrs={'style': 'text-transform: capitalize;'})
    )
    fecha = forms.DateField(
        required=True,
        label='Fecha',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        required=True,
        label='Producto',
        widget=forms.Select(attrs={'style': 'text-transform: capitalize;'})
    )
    cantidad = forms.IntegerField(
        required=True,
        label='Cantidad',
        widget=forms.NumberInput(attrs={'type': 'number'})
    )


    class Meta:
        model = Compra
        fields = ['estado', 'proveedor', 'fecha', 'producto', 'cantidad']
