from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.contrib import messages

from .models import Tarjeta, Transaccion
from .forms import AgregarTarjetaForm, TransaccionForm

from .mixins import LoginRequiredMixin


class HomeIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeIndexView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Bienvenido a CreditTrack ' + self.request.user.username
        context['tarjetas'] = Tarjeta.objects.filter(usuario=self.request.user)
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
        return super(TarjetaCreateView, self).form_valid(form)


class TarjetaDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'tarjetas/mostrar_detalles.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TarjetaDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Detalles de Tarjeta'
        context['tarjeta'] = Tarjeta.objects.get(id=self.kwargs['pk'])
        context['transacciones_form'] = TransaccionForm(initial={'tarjeta': Tarjeta.objects.get(id=self.kwargs['pk'])})
        context['transacciones'] = Transaccion.objects.filter(tarjeta=self.kwargs['pk']).order_by('-fecha')
        context['monto_diferencia'] = int(context['tarjeta'].monto_maximo) - int(context['tarjeta'].monto_utilizado)
        return context


class TarjetaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarjeta
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return super(TarjetaDeleteView, self).delete(request, *args, **kwargs)


class TransaccionCreateView(LoginRequiredMixin, CreateView):
    form_class = TransaccionForm
    template_name = 'transacciones/agregar_transaccion.html'

    def post(self, request, *args, **kwargs):
        pagina_actual = request.META.get('HTTP_REFERER')
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transaccion agregada correctamente')
        else:
            messages.error(request, 'Error al agregar transaccion')
            return super(TransaccionCreateView, self).post(request, *args, **kwargs)
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