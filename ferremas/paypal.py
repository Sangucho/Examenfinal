from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
import paypalrestsdk
import logging
import requests
import math


paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  # sandbox o live
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

def create_payment (request):
    
    if request.method == 'POST':
        print("hola")
        try:

            #OBTENER CLP A DONAR
            cantidadCLP = int(request.POST.get('cantidad'))

            #OBTENER ULTIMA CONVERSION A DOLAR DE API 
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")

            if response.status_code == 200:
                exchange_rates = response.json()['rates']
                clp_to_usd_rate = exchange_rates.get('CLP')
                
                
                if clp_to_usd_rate:
                    cantidad_usd = cantidadCLP / clp_to_usd_rate
                    #TRUNCAR A 2 DECIMALES
                    cantidad_usd = math.floor(cantidad_usd * 100) / 100
                    if cantidad_usd > 0:
                        payment = paypalrestsdk.Payment({
                            "intent": "sale",
                            "payer": {
                                "payment_method": "paypal"
                            },
                            "redirect_urls": {
                                "return_url": "https://chimiclips.xyz/payment/execute/",
                                "cancel_url": "https://chimiclips.xyz/payment/cancel/"
                            },
                            "transactions": [{
                                "item_list": {
                                    "items": [{
                                        "name": "Donacion",
                                        "sku": "donation",
                                        "price": cantidad_usd,
                                        "currency": "USD",
                                        "quantity": 1
                                    }]
                                },
                                "amount": {
                                    "total": cantidad_usd,
                                    "currency": "USD"
                                },
                                "description": "Donación voluntaria"
                            }]
                        })

                        if payment.create():
                            for link in payment.links:
                                if link.rel == "approval_url":
                                    approval_url = str(link.href)
                                    return redirect(approval_url)
                        else:
                            logging.error(payment.error)
        except Exception:
            import traceback
            traceback.print_exc()
            #error durante el proceso de crear metodo de pago
            return redirect('inicio')
        #solicitud incorrecta solo permite POST
    return redirect('inicio')

def cancel_payment(request):
    return render(request, 'payment/cancel.html')

def execute_payment (request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        response_data = {
            "status": "success",
            "payment_id": payment.id,
            "payer_id": payer_id,
            "transactions": payment.transactions
        }
        return JsonResponse(response_data)
    else:
        logging.error(payment.error)
        response_data = {
            "status": "error",
            "error": payment.error
        }
        return JsonResponse(response_data)