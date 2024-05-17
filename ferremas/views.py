from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

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
                return redirect('login')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'contraseñas no coinciden'
        })

def login(request):
    return render(request, 'login.html')

def agregarproducto(request):
    return render(request, 'AgregarProducto.html')

def editarproducto(request):
    return render(request, 'EditarProducto.html')

def editarproducto(request):
    return render(request, 'PerfilUsuario.html')