from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def inicioAdmin(request):
    return render(request, 'inicioAdmin.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir al usuario a una página de éxito
            return redirect('inicio.html')  # Reemplaza 'index' con el nombre de tu vista de inicio
        else:
            # Mostrar un mensaje de error
            return render(request, 'login.html', {'error_message': 'Credenciales inválidas.'})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir al usuario a una página de éxito
            return redirect('inicio.html')  # Reemplaza 'index' con el nombre de tu vista de inicio
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def agregarproducto(request):
    return render(request, 'AgregarProducto.html')

def editarproducto(request):
    return render(request, 'EditarProducto.html')
