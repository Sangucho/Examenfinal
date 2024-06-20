import requests
from django.http import HttpResponse
import json



def find_all():

    print('find_all')
    url = 'http://127.0.0.1:8000/api/product'
    response = requests.get(url)
    response.encoding = 'utf-8'
    print('response: {0}'.format(response))
    print('status: {0}'.format(response.status_code))
    if response.status_code == 200:
        print('JSON: {0}'.format(response.json()))
        return response.json()
    else:
        print('message: {0}'.format(response.text))
        raise Exception('message')


def add_producto(request):
    print('add_producto')   
    url = 'http://127.0.0.1:8000/api/product'
    try:    
            nombre = request.POST['nombre']
            descripcion = request.POST['descripcion']
            precio = request.POST['precio']
            stock = request.POST['stock']

            json = {
                    "nombre": nombre,
                    "descripcion": descripcion,
                    "precio": precio,
                    "stock": stock,
                }

            print(json)
            response = requests.post(url, json=json)
            response.encoding = 'utf-8' 
            print('response code: {0}'.format(response.status_code))
            print('response body -> {0}'.format(response.json()))
            

            if response.json() == 204:
                
                return 204
            if response.status_code == 200:
                return 200

    except Exception as e:
        print("ERROR INVOCACIÓN SERVICIO : {0}, {1}".format(url, e)) 

def delete_by_id(id):
    print('delete_by_id')   
    url = 'http://127.0.0.1:8000/api/product/{0}'.format(id)
    try:
        response = requests.delete(url)
        print('response code: {0}'.format(response.status_code))
        print('response code: {0}'.format(response.text))
    except Exception as e:
        print("ERROR INVOCACIÓN SERVICIO : {0}, {1}".format(url, e))     


def update_producto(request): 
    url = 'http://127.0.0.1:8000/api/product'
    try:
        id = request.POST["id"]
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']

        json = {
                "id": id,
                "nombre": nombre,
                "descripcion": descripcion,
                "precio": precio,
                "stock": stock,
            }

        print(json)
        response = requests.put(url, json=json)
        print('response code: {0}'.format(response.status_code))
        print('response body -> {0}'.format(response.json()))

    except Exception as e:
        print("ERROR INVOCACIÓN SERVICIO : {0}, {1} , No se recibieron los datos necesarios".format(url, e)) 






# ferremas/lib/integracionapi.py

import requests

def find_all_carrito():
    print('find_all_carrito')
    url = 'http://127.0.0.1:8000/api/carrito'
    response = requests.get(url)
    response.encoding = 'utf-8'
    print('response: {0}'.format(response))
    print('status: {0}'.format(response.status_code))
    if response.status_code == 200:
        print('JSON: {0}'.format(response.json()))
        return response.json()
    else:
        error_message = f'Error {response.status_code}: {response.text}'
        print(error_message)
        raise Exception(error_message)



def add_producto_carrito(request):
    print('add_producto_carrito')   
    url = 'http://127.0.0.1:8000/api/carrito'
    try:    

            id = request.POST['id']
            producto = request.POST['producto']
            cantidad = request.POST['cantidad']
            precio = request.POST['precio']

            json = {
                    "id": id,
                    "producto": producto,
                    "cantidad": cantidad,
                    "precio": precio
                }

            print(json)
            response = requests.put(url, json=json)
            response.encoding = 'utf-8' 
            print('response code: {0}'.format(response.status_code))
            print('response body -> {0}'.format(response.json()))

    except Exception as e:
        print("ERROR INVOCACIÓN SERVICIO : {0}, {1}".format(url, e)) 




def preciocarrito():

    print('find_all')
    url = 'http://127.0.0.1:8000/api/sumarcarrito'
    response = requests.get(url)
    response.encoding = 'utf-8'
    print('response: {0}'.format(response))
    print('status: {0}'.format(response.status_code))
    if response.status_code == 200:
        print('JSON: {0}'.format(response.json()))
        return response.json()
    else:
        print('message: {0}'.format(response.text))
        raise Exception('message')

def contarcarrito():

    print('contarcarrito')
    url = 'http://127.0.0.1:8000/api/contarcarrito'
    response = requests.get(url)
    response.encoding = 'utf-8'
    print('response: {0}'.format(response))
    print('status: {0}'.format(response.status_code))
    if response.status_code == 200:
        print('JSON: {0}'.format(response.json()))
        return response.json()
    else:
        print('message: {0}'.format(response.text))
        raise Exception('message')









def recuperar_carrito(dic):
    print('recuperar_carrito')   
    url = 'http://127.0.0.1:8000/api/stock'
    try:    

            

            

            print(dic)
            response = requests.put(url, json=dic)
            response.encoding = 'utf-8' 
            print('response code: {0}'.format(response.status_code))
            print('response body -> {0}'.format(response.json()))

    except Exception as e:
        print("ERROR INVOCACIÓN SERVICIO : {0}, {1}".format(url, e)) 



def delete_carrito_by_id(id):
    print('delete_by_id')   
    url = 'http://127.0.0.1:8000/api/carrito/{0}'.format(id)
    try:
        response = requests.delete(url)
        print('response code: {0}'.format(response.status_code))
        print('response code: {0}'.format(response.text))
    except Exception as e:
        print("ERROR INVOCACIÓN SERVICIO : {0}, {1}".format(url, e)) 



def add_algo(request):
    print('add_producto')   
    url = 'http://127.0.0.1:8000/api/nada'
    try:    


            my_list = []

            if 'diccionario' in request.POST:

                my_list = request.POST['diccionario']


            json = {
                    "nada": my_list,

                }

            print(json)
            response = requests.post(url, json=json)
            response.encoding = 'utf-8' 
            print('response code: {0}'.format(response.status_code))
            print('response body -> {0}'.format(response.json()))

    except Exception as e:
        print("ERROR INVOCACIÓN SERVICIO : {0}, {1}".format(url, e))   


def delete_algo():
    print('delete_algo')   
    url = 'http://127.0.0.1:8000/api/nada'
    try:
        response = requests.delete(url)
        print('response code: {0}'.format(response.status_code))
        print('response code: {0}'.format(response.text))
    except Exception as e:
        print("ERROR INVOCACIÓN SERVICIO : {0}, {1}".format(url, e)) 



def find_all_anonyy():

    print('find_all')
    url = 'http://127.0.0.1:8000/api/nada'
    response = requests.get(url)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        print('JSON: {0}'.format(response.json()))
        return response.json()
    else:
        print('message: {0}'.format(response.text))
        raise Exception('message')



def limpiar_carrito():
    print('delete_algo')   
    url = 'http://127.0.0.1:8000/api/carrito'
    try:
        response = requests.delete(url)
        print('response code: {0}'.format(response.status_code))
        print('response code: {0}'.format(response.text))
    except Exception as e:
        print("ERROR INVOCACIÓN SERVICIO : {0}, {1}".format(url, e)) 