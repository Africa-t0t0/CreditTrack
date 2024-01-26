import requests

from django.db.models import Avg
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from credittrack.settings import api_currency

from credittrack.utils import funcion_meses, nombre_meses

from .utils import obtener_tipo_cambio
from .forms import CompraForm
from .models import Compra

class ContenedoresHomeView(TemplateView):
    template_name = 'exterior/contenedores_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cambio_usd, cambio_eur, cambio_jpy = obtener_tipo_cambio("USD", "CLP", valor=1)
        dict = {'USD': cambio_usd, 'EUR': cambio_eur, 'JPY': cambio_jpy}
        meses, anio = funcion_meses()
        monto_mensual = []
        cantidad_mensual = []
        print('meses', meses)
        for mes in meses:
            if meses[len(meses) - 1] < meses[0]:
                anio_temp = anio - 1
            else:
                anio_temp = anio
            compras = Compra.objects.filter(usuario=self.request.user, fecha__month=mes, fecha__year=anio_temp)
            compra_monto = compras.aggregate(promedio=Avg('total'))
            if compra_monto['promedio'] == None:
                compra_monto['promedio'] = 0
            cantidad_mensual.append(compras.count())
            monto_mensual.append(compra_monto['promedio'])
        print(monto_mensual)

        compras = Compra.objects.filter(usuario=self.request.user).order_by('-fecha')
        if compras.count() < 3:
            context['compras'] = compras
        else:
            context['compras'] = compras[:3]
        context['titulo'] = 'Resumen General'
        context['cambios'] = dict
        context['monto_mensual'] = monto_mensual
        context['ultimos_5_meses'] = nombre_meses(meses)
        return context


class ContenedoresCreateView(CreateView):
    model = Compra
    template_name = 'exterior/contenedores_create.html'
    form_class = CompraForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Compra'
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.total = form.instance.producto.precio * form.instance.cantidad
        return super().form_valid(form)