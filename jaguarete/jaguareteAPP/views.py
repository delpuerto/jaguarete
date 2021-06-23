from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CustomUserCreationForm, ContactoForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# PAGINA INICIAL
def index(request):
    return render(request,"home/index.html")


# PAGINA ACERCA DE
def acerca(request):
    return render(request,"home/acerca.html")


# PAGINA CONTACTO
def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado!"
        else:
            data["form"] = formulario

    return render(request,"home/contacto.html", data)



# REGISTRO DE USUARIOS
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
