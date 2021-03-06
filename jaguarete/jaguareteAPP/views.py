from .carro import Carro
from django.core import paginator
from django.http.response import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import CustomUserCreationForm, ContactoForm, ProductoForm, CategoriaForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Categoria, Producto
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required, user_passes_test




# PAGINA INICIAL ---------------------------------------------------------------
def index(request):
    productos = Producto.objects.all().order_by('-id')[:3]
    todos     = Producto.objects.all()
    page      = request.GET.get('page', 1)

    try:
        paginator = Paginator(todos, 3)
        todos     = paginator.page(page)
    except:
        raise Http404

    data = {
        'productos': productos,
        'entity': todos,
        'paginator': paginator 
    }
    return render(request,"home/index.html", data)



# PAGINA ACERCA DE -------------------------------------------------------------
def acerca(request):
    return render(request,"home/acerca.html")



# PAGINA CONTACTO --------------------------------------------------------------
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje de contacto Guardado correctamente")
            data["mensaje"] = "Contacto Guardado!"
        else:
            data["form"] = formulario
    return render(request,"home/contacto.html", data)



# REGISTRO DE USUARIOS ---------------------------------------------------------
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




#==============================================================================
# PAGINA LISTAR PRODUCTO
def listar_productos(request):
    productos = Producto.objects.all()
    page      = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 3)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': productos ,
        'paginator': paginator
    }
    return render(request,"producto/listar.html", data)



# PAGINA AGREGAR PRODUCTO
@user_passes_test(lambda u: u.is_staff)
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente!"
            messages.success(request, "Guardado correctamente")
        else:
            data["form"] = formulario
    return render(request,"producto/agregar.html", data)



# PAGINA MODIFICAR PRODUCTO
@user_passes_test(lambda u: u.is_staff)
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se modifico correctamente")
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario
    return render(request,"producto/modificar.html", data)



# PAGINA ELIMINAR PRODUCTO
@user_passes_test(lambda u: u.is_staff)
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_productos")





#==============================================================================
# PAGINA LISTAR CATEGORIA
def listar_categorias(request):
    categoria = Categoria.objects.all()
    data = {
        'categorias': categoria 
    }
    return render(request,"categoria/listar.html", data)



# PAGINA AGREGAR CATEGORIA
@user_passes_test(lambda u: u.is_staff)
def agregar_categoria(request):
    data = {
        'form': CategoriaForm()
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente!"
            messages.success(request, "Guardado correctamente")
        else:
            data["form"] = formulario
    return render(request,"categoria/agregar.html", data)



# PAGINA MODIFICAR CATEGORIA
@user_passes_test(lambda u: u.is_staff)
def modificar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    data = {
        'form': CategoriaForm(instance=categoria)
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_categorias")
        else:
            data["form"] = formulario
    return render(request,"categoria/modificar.html", data)



# PAGINA ELIMINAR CATEGORIA
@user_passes_test(lambda u: u.is_staff)
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, "Eliminada correctamente")
    return redirect(to="listar_categorias")






# PAGINA Mostrar producto
# @user_passes_test(lambda u: u.is_authenticated)
def mostrar_producto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'producto': producto 
    }
    return render(request,"producto/mostrar.html", data)




# PAGINA Resultado ---------------------------------------------------------------
def resultado(request):
    todos = ""    
    txt   = ""
    if request.method == 'POST':
        txt = request.POST.get("busk")
    
    if txt:
        todos = Producto.objects.filter(nombre__contains=txt)
        data = {
            'res': todos,
            'texto': "resultados de la busqueda: '" + txt + "'"
        }
    else:
        data = {
            'res': todos,
            'texto': "No se encontro resultado con el criterio buscado" 
        }
    return render(request,"home/resultados.html", data)



# Agregar Producto al carro ------------------------------------------------------
@user_passes_test(lambda u: u.is_authenticated)
def agregarProducto(request, id):
    producto = Producto.objects.get(id=id)
    carro = Carro(request)
    carro.agregar(producto)
    messages.success(request, "Producto agregado al carro de compras!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



# Restar Producto al carro ------------------------------------------------------
@user_passes_test(lambda u: u.is_authenticated)
def restar_producto(request, id):
    producto = Producto.objects.get(id=id)
    carro = Carro(request)
    carro.restar_producto(producto)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



# Vaciar Productos del carro ------------------------------------------------------
@user_passes_test(lambda u: u.is_authenticated)
def vaciar_producto(request):
    carro = Carro(request)
    carro.vaciar()
    messages.success(request, "Has vaiado el carro de compras :-(")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



# PAGINA Carrito -----------------------------------------------------------------
@user_passes_test(lambda u: u.is_authenticated)
def carrito(request):
    return render(request,"home/carrito.html")






# PAGINA Busca Categoria ---------------------------------------------------------------
def bus_cat(request, categoria_nombre):
    todos = ""    
    txt   = categoria_nombre
    
    if txt:
        todos = Producto.objects.filter(categoria=txt)
        data = {
            'res': todos,
            'texto': ""
        }
    else:
        data = {
            'res': todos,
            'texto': "No se encontro resultado con el criterio buscado" 
        }
    return render(request,"home/resultados.html", data)
