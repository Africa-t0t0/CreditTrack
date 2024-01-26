from django.urls import path

from .views import *

app_name = 'exterior'

urlpatterns = [
    path('', ContenedoresHomeView.as_view(), name='contenedores_home'),
    path('compras/crear/', ContenedoresCreateView.as_view(), name='contenedores_crear'),
]