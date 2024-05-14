from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def inicioAdmin(request):
    return render(request, 'inicioAdmin.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def agregarproducto(request):
    return render(request, 'AgregarProducto.html')
