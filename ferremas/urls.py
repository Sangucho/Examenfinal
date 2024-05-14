from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('/inicioAdmin', views.inicioAdmin, name='inicioAdmin'),
    path('/login', views.login, name='login'),
    path('/register', views.register, name='register'),
    path('/agregarproducto', views.agregarproducto, name='agregarproducto'),
]