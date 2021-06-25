from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca', views.acerca, name="acerca"),
    path('contacto', views.contacto, name="contacto"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name="registro"),
    path('agregar_producto/', views.agregar_producto, name="agregar_producto"),
    path('listar_productos/', views.listar_productos, name="listar_productos"),
]
