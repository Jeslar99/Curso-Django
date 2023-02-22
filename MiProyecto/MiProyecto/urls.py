"""MiProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from MiProyecto.views import bienvenida, bienvenidaRojo
from MiProyecto.views import categoriaEdad, obtenerMomentoActual, contenidoHTML
from MiProyecto.views import miPrimeraPlantilla, plantillaParametros, plantillaCargador, plantillaShortcut,plantillaHija1, plantillaHija2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('bienvenida123/', bienvenidaRojo),
    path('categoria/<int:edad>', categoriaEdad),
    path('obtenerMomentoActual/', obtenerMomentoActual),
    path('contenidoHTML/<nombre>/<int:edad>', contenidoHTML),
    path('miPrimeraPlantilla/', miPrimeraPlantilla),
    path('plantillaParametros/', plantillaParametros),
    path('plantillaCargador/', plantillaCargador),
    path('plantillaShortcut/', plantillaShortcut),
    path('plantillaHija1/', plantillaHija1),
    path('plantillaHija2/', plantillaHija2),

]
