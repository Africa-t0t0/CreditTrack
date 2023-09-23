"""
URL configuration for credittrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from .views import *

from .login import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("select2/", include("django_select2.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', HomeIndexView.as_view(), name='home'),
    path('tarjeta/crear', TarjetaCreateView.as_view(), name='tarjeta_crear'),
    path('tarjeta/detalles/<int:pk>', TarjetaDetailView.as_view(), name='tarjeta_detalles'),
    path('tarjeta/eliminar/<int:pk>', TarjetaDeleteView.as_view(), name='tarjeta_eliminar'),
    path('tarjeta/mostrar_tarjetas', TarjetaListView.as_view(), name='tarjeta_mostrar_tarjetas'),
    path('transaccion/crear/<int:pk>', TransaccionCreateView.as_view(), name='transaccion_crear'),
    path('transaccion/eliminar/<int:pk>', TransaccionDeleteView.as_view(), name='transaccion_eliminar'),
    path('transaccion/editar/<int:pk>', TransaccionUpdateView.as_view(), name='transaccion_editar'),
]
