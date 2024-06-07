# currency/urls.py
from django.urls import path
from .views import show_exchange_rate

urlpatterns = [
    path('exchange-rate/', show_exchange_rate, name='exchange_rate'),
]
