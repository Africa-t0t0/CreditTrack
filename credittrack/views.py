from django.shortcuts import render
from django.views.generic import TemplateView

class HomeIndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeIndexView, self).get_context_data(*args, **kwargs)
        return context