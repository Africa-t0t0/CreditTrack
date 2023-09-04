from django.shortcuts import render
from django.views.generic import TemplateView

class HomeIndexView(TemplateView):
    def get(self, request):
        return render(request, 'index.html')