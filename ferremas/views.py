from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError
from . models import Producto

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def inicioAdmin(request):
    return render(request, 'inicioAdmin.html')

def registro(request):

    if request.method == 'GET':
        return render(request, 'registro.html',{
        'form': UserCreationForm
        })
    else:
        if request.POST ['password1'] == request.POST['password1']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('signin')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'contraseñas no coinciden'
        })

def singin(request):
    return render(request, 'login.html')

def agregarproducto(request):
    if request.method == 'POST':
        # Procesar los datos del formulario de agregar producto
        nombreart = request.POST.get('nombreart')
        marca = request.POST.get('marca')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        imagen = request.FILES.get('imagen')

        # Aquí puedes guardar los datos en la base de datos
        Producto.objects.create(
            nombreart=nombreart,
            marca=marca,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            imagen=imagen,
        )
        messages.success(request, f'El artículo {nombreart} se añadió con éxito')
        return render(request, 'AgregarProducto.html')

    return render(request, 'AgregarProducto.html')

def editarproducto(request):
    return render(request, 'EditarProducto.html')

def editarproducto(request):
    return render(request, 'PerfilUsuario.html')

def cerrarSesion(request):
    logout(request)
    return redirect('inicio')