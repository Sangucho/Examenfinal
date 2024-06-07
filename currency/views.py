from django.shortcuts import render
from django.shortcuts import render
from .services import get_usd_clp_exchange_rate

def show_exchange_rate(request):
    try:
        exchange_rate = get_usd_clp_exchange_rate()
    except Exception as e:
        exchange_rate = None
        error = str(e)
    return render(request, 'currency/exchange_rate.html', {'exchange_rate': exchange_rate, 'error': error})

def convert_price_to_usd(price_clp):
    try:
        exchange_rate = get_usd_clp_exchange_rate()
        price_usd = price_clp / exchange_rate
        return price_usd
    except Exception as e:
        return None
