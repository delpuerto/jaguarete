from django.shortcuts import render
from django.http import HttpResponse

# Definicion de Vistas.
def index(request):
    # return HttpResponse("hola Mundo!")
    return render(request,"home/index.html")

def acerca(request):
    return HttpResponse("del Puerto Software (c)2021")

     