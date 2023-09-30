from django.db.models import Avg, Count
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, View
from django.contrib import messages
from datetime import datetime
from dateutil.relativedelta import relativedelta

from .models import Tarjeta, Transaccion
from .forms import AgregarTarjetaForm, TransaccionForm
from .utils import funcion_meses, nombre_meses

from .mixins import LoginRequiredMixin


class HomeIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeIndexView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Bienvenido a CreditTrack ' + self.request.user.username
        context['tarjetas'] = Tarjeta.objects.filter(usuario=self.request.user)
        meses, anio = funcion_meses()
        context['ultimos_5_meses'] = nombre_meses(meses)
        monto_mensual = []
        cantidad_mensual = []
        for mes in meses:
            transaccion = Transaccion.objects.filter(tarjeta__usuario=self.request.user, fecha__month=mes, fecha__year=anio)
            transaccion_monto = transaccion.aggregate(promedio=Avg('monto'))
            if transaccion_monto['promedio'] == None:
                transaccion_monto['promedio'] = 0
            cantidad_mensual.append(transaccion.count())
            monto_mensual.append(transaccion_monto['promedio'])
        context['monto_mensual'] = monto_mensual
        context['cantidad_mensual'] = cantidad_mensual
        return context


class TarjetaListView(LoginRequiredMixin, TemplateView):
    template_name = 'tarjetas/mostrar_tarjetas.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TarjetaListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Mis Tarjetas'
        context['tarjetas'] = Tarjeta.objects.filter(usuario=self.request.user)
        return context


class TarjetaCreateView(LoginRequiredMixin, CreateView):
    model = Tarjeta
    form_class = AgregarTarjetaForm
    template_name = 'tarjetas/agregar_tarjeta.html'
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super(TarjetaCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Agregar Tarjeta'
        context['form'] = AgregarTarjetaForm()
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.monto_utilizado = 0
        return super(TarjetaCreateView, self).form_valid(form)


class TarjetaDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'tarjetas/mostrar_detalles.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TarjetaDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Detalles de Tarjeta'
        context['tarjeta'] = Tarjeta.objects.get(id=self.kwargs['pk'])
        context['transacciones_form'] = TransaccionForm(initial={'tarjeta': Tarjeta.objects.get(id=self.kwargs['pk'])})
        context['transacciones'] = Transaccion.objects.filter(tarjeta=self.kwargs['pk']).order_by('-fecha')
        if context['tarjeta'].monto_maximo != None and context['tarjeta'].monto_utilizado != None:
            context['monto_diferencia'] = int(context['tarjeta'].monto_maximo) - int(context['tarjeta'].monto_utilizado)
        return context


class TarjetaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarjeta
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('home')


class TransaccionCreateView(LoginRequiredMixin, View):
    form_class = TransaccionForm

    def post(self, request, *args, **kwargs):
        pagina_actual = request.META.get('HTTP_REFERER')
        print('recibimos uwu')
        form = TransaccionForm(request.POST)
        if form.is_valid():
            print('es valido uwu')
            form.save()
            messages.success(request, 'Transaccion agregada correctamente')
        else:
            print('no es valido uwu', form.errors)
            messages.error(request, 'Error al agregar transaccion')
        return redirect(pagina_actual)


class TransaccionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaccion

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(request, 'Transaccion eliminada correctamente')
        return redirect('tarjeta_detalles', pk=self.object.tarjeta.id)


class TransaccionUpdateView(LoginRequiredMixin, UpdateView):
    pass