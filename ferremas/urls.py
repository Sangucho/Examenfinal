from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicioAdmin/', views.inicioAdmin, name='inicioAdmin'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('agregarproducto/', views.agregarproducto, name='agregarproducto'),
    path('editarproducto/',views.editarproducto, name='editarproducto'),
    path('perfilusuario/',views.editarproducto, name='perfilusuario'),
]
