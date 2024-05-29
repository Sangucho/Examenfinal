from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from . models import Producto
from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.

def inicio(request):
    # Obtener todos los productos
    productos = Producto.objects.all()
    if request.user.is_authenticated and request.user.username.endswith('@ferremas.com'):
        mostrar_boton_agregar = True
    else:
        mostrar_boton_agregar = False

    return render(request, 'inicio.html', {'productos': productos, 'mostrar_boton_agregar': mostrar_boton_agregar})

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form': UserCreationForm})
    else:
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                username = request.POST.get('username')
                if username.endswith('@ferremas.com'):
                    user = User.objects.create_user(
                        username=username,
                        password=request.POST.get('password1'))
                    user.save()
                    login(request, user)
                    return redirect('inicio')
                else:
                    return render(request, 'registro.html', {
                        'form': UserCreationForm,
                        'error': 'El nombre de usuario debe terminar con "@ferremas.com"'
                    })
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'Usuario o contraseña incorrecto'})
        else:
            login(request, user)
            return redirect('inicio')

        
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
 
 # Monto a cobrar en centavos ($1.00)

from .fakepay import fakepay_process_payment  # Ajusta la importación según la ubicación real

fakepay_api_key = 'your_fakepay_api_key'
fakepay_amount = 100  # Ajusta el monto según sea necesario

@csrf_exempt  # Solo si estás probando sin protección CSRF, no uses esto en producción
def process_payment(request):
    if request.method == 'POST':
        # Datos del formulario
        card_number = request.POST['card_number']
        expiry_date = request.POST['expiry_date']
        cvv = request.POST['cvv']

        # Procesamiento del pago utilizando la pasarela de pago FakePay (ejemplo)
        response = fakepay_process_payment(fakepay_api_key, fakepay_amount, card_number, expiry_date, cvv)

        # Verificación de la respuesta de la pasarela de pago
        if response['success']:
            # El pago fue exitoso
            return HttpResponse("¡El pago se ha realizado correctamente!")
        else:
            # El pago falló
            return HttpResponse("Lo siento, ha ocurrido un error durante el procesamiento del pago: " + response['error'])
    
    # Si la solicitud no es POST, renderiza el formulario de pago
    return render(request, 'payment_form.html')