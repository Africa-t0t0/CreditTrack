from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView

from .models import Tarjeta
from .forms import AgregarTarjetaForm

from .mixins import LoginRequiredMixin


class HomeIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeIndexView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Bienvenido a CreditTrack ' + self.request.user.username
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
        return context


class TarjetaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarjeta
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return super(TarjetaDeleteView, self).delete(request, *args, **kwargs)