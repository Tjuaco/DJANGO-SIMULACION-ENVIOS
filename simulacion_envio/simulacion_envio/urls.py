"""
URL configuration for simulacion_envio project.

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
from django.urls import path
from simulacion_envio_app import views
app_name = 'simulacion_envio_app'

#RUTAS
urlpatterns = [

    path('admin/', admin.site.urls),#PANEL ADMIN


    path('', views.inicio, name='inicio'),#PAGINA DE EINICIO


    path('Formulario/', views.crear_simulacion_form, name='crear_simulacion_form'),#MOSTRAR FORMULARIO DE CREACION


    path('Resultado/', views.enviar_simulacion_form, name='enviar_simulacion_form'),#ENVIAR FORMULARIO Y CALCULAR


    path('lista_simulaciones/', views.ListaSimulacionesView.as_view(), name='lista_simulaciones'),#MOSTRAR LISTA DE SIMUACIONES


    path('resultados/', views.enviar_simulacion_form, name='resultados_simulacion'),#MOSTRAR RESULTADOS


    path('eliminar_simulacion/<int:id>/', views.eliminar_simulacion, name='eliminar_simulacion'),#ELIMINAR SIMULACIONES
]
