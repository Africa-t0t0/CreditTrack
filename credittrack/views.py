from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

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