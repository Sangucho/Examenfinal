from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from . models import Producto
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction

from .lib.integracionapi import add_producto, find_all, delete_by_id, update_producto, add_producto_carrito, find_all_carrito, preciocarrito, recuperar_carrito, delete_carrito_by_id, add_algo, delete_algo, find_all_anonyy, limpiar_carrito

from transbank.common.options import WebpayOptions
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
import json
import random
from django.views.decorators.csrf import csrf_exempt
import datetime as dt

import requests
# Create your views here.

def apimiindicador():
    url = 'https://mindicador.cl/api'
    response = requests.get(url).json()
    return response

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


"""Carrito metodos"""
def carrito(request):
    try:
        # productosca = find_all_carrito()

        # precios = preciocarrito()
        # total =  sum(precios)
        # response = apimiindicador()

        return render(request, "carrito.html")
    except Exception as e:
        print("error: " + str(e))
        return HttpResponse(f"Error al cargar el carrito: {str(e)}", status=500)
    
def agregar_producto_al_carrito(request):
    if request.method == "POST":
        add_producto_carrito(request)
        productos2 = find_all()
        response = apimiindicador()
    return render(request, 'catalogo.html', {'productos': productos2, 'response': response})



def recuperar_datos_carrito(request):
    if request.method == "POST":
        pass

    productosca = find_all_carrito()

    precios = preciocarrito()
    total =  sum(precios)

    response = apimiindicador()

    return render(request, "carritocompras.html", {'productosca': productosca, 'total':total, 'response': response})





def eliminar_del_carrito(request):
    if request.method == "GET":
        delete_carrito_by_id(request.GET['id'])
        productosca = find_all_carrito()
        precios = preciocarrito()
        total =  sum(precios)
        response = apimiindicador()
    return render(request, 'carritocompras.html', {'productosca': productosca, 'total':total, 'response': response})


def cerrarSesion(request):
    logout(request)
    return redirect('inicio')

def error(request):
    return render(request, "transbank/error.html")

def rechazo(request):
    return render(request, "transbank/rechazada.html")

def webpay_plus_create(request):
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = request.POST.get('total')
    return_url = 'http://localhost:8000/' + 'commit-webpay'

    add_algo(request)

    
    tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY))

    response = tx.create(buy_order, session_id, amount, return_url)

    print(response)

    return render(request, 'transbank/crear.html', {'response': response, 'amount': amount})

@csrf_exempt
def webpay_plus_commit(request):
    print('commitpay')
    print("request: {0}".format(request.POST))    
    token = request.GET.get('token_ws')

    TBK_TOKEN = request.POST.get('TBK_TOKEN')
    TBK_ID_SESION = request.POST.get('TBK_ID_SESION')
    TBK_ORDEN_COMPRA = request.POST.get('TBK_ORDEN_COMPRA')

    #TRANSACCIÓN REALIZADA
    if TBK_TOKEN is None and TBK_ID_SESION is None and TBK_ORDEN_COMPRA is None and token is not None:

        #APROBAR TRANSACCIÓN
        tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY))
        response = tx.commit(token=token)
        print("response: {}".format(response)) 

        status = response.get('status')
        print("status: {0}".format(status))
        response_code = response.get('response_code')
        print("response_code: {0}".format(response_code)) 
        #TRANSACCIÓN APROBADA
        if status == 'AUTHORIZED' and response_code == 0:

            state = ''
            if response.get('status') == 'AUTHORIZED':
                state = 'Aceptado'
            pay_type = ''
            if response.get('payment_type_code') == 'VD':
                pay_type = 'Tarjeta de Débito'
            amount = int(response.get('amount'))
            amount = f'{amount:,.0f}'.replace(',', '.')
            transaction_date = dt.datetime.strptime(response.get('transaction_date'), '%Y-%m-%dT%H:%M:%S.%fZ')
            transaction_date = '{:%d-%m-%Y %H:%M:%S}'.format(transaction_date)
            transaction_detail = {  'card_number': response.get('card_detail').get('card_number'),
                                    'transaction_date': transaction_date,
                                    'state': state,
                                    'pay_type': pay_type,
                                    'amount': amount,
                                    'authorization_code': response.get('authorization_code'),
                                    'buy_order': response.get('buy_order'), }
            hmm = find_all_anonyy()

            hmm = json.dumps(hmm)
            recuperar_carrito(hmm)

            delete_algo()
            limpiar_carrito()


            return render(request, 'transbank/commit.html', {'transaction_detail': transaction_detail})
        else:
        #TRANSACCIÓN RECHAZADA
            delete_algo()   
            return render(request, 'transbank/rechazada.html')
    else:
    #TRANSACCIÓN CANCELADA
        delete_algo()              
        return render(request, 'transbank/error.html')



#API

#PAGINA API
def productos_api(request):
    return render(request, 'productos_api.html')

from rest_framework import viewsets
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer