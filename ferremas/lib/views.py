from django.shortcuts import render
from django.http import HttpResponse
from .forms import PrductoForm
import requests
from .integracionapi import add_producto, find_all, delete_by_id, update_producto, add_producto_carrito, find_all_carrito, preciocarrito, recuperar_carrito, delete_carrito_by_id, add_algo, delete_algo, find_all_anonyy, limpiar_carrito
import random
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction

from transbank.common.options import WebpayOptions
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
import json

from django.views.decorators.csrf import csrf_exempt
import datetime as dt
from django.contrib import messages










def apimiindicador():
    url = 'https://mindicador.cl/api'
    response = requests.get(url).json()
    return response




def home(request):
    response = apimiindicador()
    return render(request,'inicio.html', {'response': response})

def carrito(request):
    productosca = find_all_carrito()

    precios = preciocarrito()
    total =  sum(precios)
    response = apimiindicador()
    
    return render(request, "carritocompras.html", {'productosca': productosca, 'total':total, 'response': response})

def login(request):
    return render(request, "login.html")

def contacto(request):
    return render(request, "contacto.html")

def productos(request):
    return render(request, "productos.html")

def error(request):
    return render(request, "transbank/error.html")

def rechazo(request):
    return render(request, "transbank/rechazada.html")

def verproductos(request):
     
    productos = find_all()
    form = PrductoForm(request.POST or None)
    

    return render(request, 'verproductos.html', {'productos': productos, 'form': form})


def catalogo(request):
     
    productos = find_all()
    response = apimiindicador()
    

    return render(request, 'catalogo.html', {'productos': productos, 'response': response})


def eliminar_producto(request):
    if request.method == "GET":
        delete_by_id(request.GET['id'])
        productos = find_all()
    return render(request, 'verproductos.html', {'productos': productos})


def editar_producto(request):
    if request.method == "POST":
        update_producto(request)
        productos = find_all()        
    return render(request, 'verproductos.html', {'productos': productos}) 




def add_product_view(request):
    mensaje = ''
    form = PrductoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        

        hola = add_producto(request)
        print(hola)
        if hola == 200:
            messages.success(request, 'Producto agregado correctamente')
        elif hola == 204:
            messages.error(request, 'El producto ya se encuentra, por favor seleccione otro o edite el stock.')
        else:
            mensaje = 'ERROR desconocido'

    
    return render(request, 'agregarproducto.html', {
        'form': form 
    

})



"""Carrito metodos"""


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

