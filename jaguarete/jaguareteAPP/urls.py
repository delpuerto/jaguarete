from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca', views.acerca, name="acerca"),
    path('home', views.home, name="home"),
    path('accounts/', include('django.contrib.auth.urls'))
]
