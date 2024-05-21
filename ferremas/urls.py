from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('signin/', views.signin, name='signin'),
    path('agregarproducto/', views.agregarproducto, name='agregarproducto'),
    path('editarproducto/',views.editarproducto, name='editarproducto'),
    path('perfilusuario/',views.editarproducto, name='perfilusuario'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
]
