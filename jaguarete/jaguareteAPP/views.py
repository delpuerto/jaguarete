from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Definicion de Vistas.
def index(request):
    # return HttpResponse("hola Mundo!")
    return render(request,"home/index.html")

def acerca(request):
    return HttpResponse("del Puerto Software (c)2021")

def registro(request):
    data={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado Correctamente")
            # redirigir al home
            return redirect(to="index")
        data["form"] = formulario

    return render(request,"registration/registro.html",data)
