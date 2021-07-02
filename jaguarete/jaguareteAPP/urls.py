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
    path('agregar_categoria/', views.agregar_categoria, name="agregar_categoria"),
    path('modificar_producto/<id>/', views.modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', views.eliminar_producto, name="eliminar_producto"),
    path('listar_categorias/', views.listar_categorias, name="listar_categorias"),
    path('modificar_categoria/<id>/', views.modificar_categoria, name="modificar_categoria"),
    path('eliminar_categoria/<id>/', views.eliminar_categoria, name="eliminar_categoria"),
    path('mostrar_producto/<id>/', views.mostrar_producto, name="mostrar_producto"),
    path('resultado/', views.resultado, name="resultado"),
    path('agregarProducto/<id>/', views.agregarProducto, name="agregarProducto"),
    path('restar_producto/<id>/', views.restar_producto, name="restar_producto"),
    path('carrito', views.carrito, name="carrito"),
    path('vaciar_producto', views.vaciar_producto, name="vaciar_producto"),
    path('bus_cat/<categoria_nombre>/', views.bus_cat, name="bus_cat"),
]
